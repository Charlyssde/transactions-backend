from rest_framework import serializers
from .models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('id', 'user_id', 'amount', 'type', 'status', 'idempotency_key', 'created_at')
        read_only_fields = ('id', 'status', 'created_at')

class TransactionProcessSerializer(serializers.Serializer):
    id = serializers.UUIDField(
        required=True,
        allow_null=False,
    )

    class Meta:
        fields = (
            "id",
        )