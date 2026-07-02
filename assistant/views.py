from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import AssistantLog
from .tasks import summarize_text_task

class SummarizeView(APIView):
    def post(self, request):
        text = request.data.get('text')
        log = AssistantLog.objects.create(input_text=text, summary="Procesando...")
        summarize_text_task.delay(text, log.id)

        return Response({"message": "Resumen en proceso", "log_id": log.id}, status=status.HTTP_202_ACCEPTED)