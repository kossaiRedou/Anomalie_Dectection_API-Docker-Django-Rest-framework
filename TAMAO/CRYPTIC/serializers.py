from rest_framework import serializers
from .models import AnomalyDetection

class AnomalyDetectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnomalyDetection
        fields = '__all__'
