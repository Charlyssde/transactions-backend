from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Transaction
from .serializers import TransactionSerializer, TransactionProcessSerializer
from .services import notify_transaction_update
from .tasks import process_transaction_task


class TransactionListView(APIView):
    def get(self, request):
        transactions = Transaction.objects.all().order_by('-created_at')
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)

class TransactionCreateView(APIView):
    def post(self, request, *args, **kwargs):
        if 'idempotency_key' not in request.data:
            return Response(
                {"error": "idempotency_key is required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        key = request.data['idempotency_key']

        existing_tx = Transaction.objects.filter(idempotency_key=key).first()
        if existing_tx:
            serializer = TransactionSerializer(existing_tx)
            return Response(serializer.data, status=status.HTTP_200_OK)

        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            transaction = serializer.save()
            notify_transaction_update(transaction)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AsyncTransactionProcessView(APIView):
    def post(self, request):
        serializer = TransactionProcessSerializer(data=request.data)
        if serializer.is_valid():
            uuid = serializer.validated_data['id']
            process_transaction_task.delay(uuid)

            return Response({
                "msg": "Transaction was successfully queued.",
                "transaction_id": uuid
            }, status=status.HTTP_202_ACCEPTED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)