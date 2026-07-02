from django.urls import path
from .views import TransactionCreateView, AsyncTransactionProcessView, TransactionListView

urlpatterns = [
    path('create/', TransactionCreateView.as_view(), name='tx-create'),
    path('async-process/', AsyncTransactionProcessView.as_view(), name='tx-async'),
    path('list/', TransactionListView.as_view(), name='transaction-list'),
]