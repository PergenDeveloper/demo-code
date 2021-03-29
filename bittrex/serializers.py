from rest_framework import serializers

from bittrex.models import BTCSummary


class BTCSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = BTCSummary
        fields = '__all__'
