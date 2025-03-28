from django.db import models

# Create your models here.
from django.db import models

class AnomalyDetection(models.Model):
    input_data = models.JSONField()
    prediction = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Anomaly: {self.prediction} at {self.created_at}"
