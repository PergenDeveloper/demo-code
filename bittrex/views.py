from rest_framework import generics

from bittrex.serializers import BTCSummarySerializer
from bittrex.models import BTCSummary


class ListBTCSummaryAPIView(generics.ListAPIView):
    queryset = BTCSummary.objects.all()
    serializer_class = BTCSummarySerializer
