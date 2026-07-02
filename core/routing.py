from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('transactions/stream/', consumers.TransactionConsumer.as_asgi()),
]