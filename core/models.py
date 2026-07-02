from django.db import models
import uuid

from core.constants import STATUS_CHOICES, Status


class Transaction(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    user_id = models.CharField(
        max_length=255,
        null=False,
        blank=False,
    )

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
    )

    type = models.CharField(
        max_length=100,
        null=False,
        blank=False,
    )
    
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=Status.PENDING,
    )

    idempotency_key = models.CharField(
        max_length=255,
        unique=True,
        null=False,
        blank=False,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_id} - {self.amount} - {self.status}"

    class Meta:
        db_table = 'transaction'
        verbose_name = 'Transaction'
        verbose_name_plural = 'Transactions'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['-created_at']),
            models.Index(fields=['user_id']),
            models.Index(fields=['idempotency_key']),
        ]