from celery import shared_task
import time
import random

from .constants import Status
from .models import Transaction


from .services import notify_transaction_update


@shared_task
def process_transaction_task(transaction_id):
    try:
        tx = Transaction.objects.get(id=transaction_id)
        time.sleep(5)

        is_success = random.choice([True, True, True, True, False])
        tx.status = Status.PROCESSED if is_success else Status.FAILED
        tx.save()

        notify_transaction_update(tx, event_type="transaction_status_changed")

    except Transaction.DoesNotExist:
        print("Error on transaction.")

pass