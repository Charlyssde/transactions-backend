# transactions/tasks.py
from celery import shared_task
from .models import AssistantLog
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from .services import get_summary


@shared_task
def summarize_text_task(text, log_id):
    channel_layer = get_channel_layer()
    error_message = "Failed to retrieve information from API."

    try:
        summary = get_summary(text)
    except Exception as e:
        print(f"Error en Celery task: {e}")
        summary = error_message

    log = AssistantLog.objects.get(id=log_id)
    log.summary = summary
    log.save()

    event_name = "summary_ready" if summary != error_message else "summary_failed"

    async_to_sync(channel_layer.group_send)(
        "transactions_updates",
        {
            "type": "transaction_update",
            "message": {
                "event": event_name,
                "data": {"log_id": log_id, "summary": summary}
            }
        }
    )