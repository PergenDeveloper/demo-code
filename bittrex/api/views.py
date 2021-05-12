from rest_framework import generics

from bittrex.api.serializers import BTCSummarySerializer
from bittrex.models import BTCSummary


class BTCSummaryListAPIView(generics.ListAPIView):
    queryset = BTCSummary.objects.all()
    serializer_class = BTCSummarySerializer
