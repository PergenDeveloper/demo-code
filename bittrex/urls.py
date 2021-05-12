from django.urls import path
from bittrex.api import views

urlpatterns = [
    path('bittrex/btc_summary', views.BTCSummaryListAPIView.as_view(), name='btc_summary'),
]
