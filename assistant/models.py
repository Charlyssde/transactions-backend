from django.db import models

class AssistantLog(models.Model):
    input_text = models.TextField(
        max_length=500,
    )
    summary = models.TextField(
        max_length=500,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        db_table = 'assistant_log'
        ordering = ['-created_at']
        verbose_name = 'Assistant Log'
        verbose_name_plural = 'Assistant Logs'
