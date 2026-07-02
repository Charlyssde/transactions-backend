from django.urls import path

from assistant.views import SummarizeView

urlpatterns = [
    path('summarize/', SummarizeView.as_view(), name='tx-summarize'),

]