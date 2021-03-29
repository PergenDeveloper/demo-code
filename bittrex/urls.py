from django.urls import path
from bittrex import views

urlpatterns = [
    path('btc/summary', views.ListBTCSummaryAPIView.as_view(), name='btc_summary'),
]
