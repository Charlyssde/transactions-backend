from core.celery import app as celery_app
from assistant.celery import app as celery_assistant

__all__ = ('celery_app', 'celery_assistant')