from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from core.models import Transaction

def notify_transaction_update(data : Transaction, event_type="transaction_created"):
    channel_layer = get_channel_layer()
    parsed_data = {
        "id" : str(data.id),
        "status" : data.status,
        "type" : data.type,
        "amount" : str(data.amount),
        "user_id" : data.user_id,
    }
    async_to_sync(channel_layer.group_send)(
        "transactions_updates",
        {
            "type": "transaction_update",
            "message": {
                "event": event_type,
                "data": parsed_data
            }
        }
    )