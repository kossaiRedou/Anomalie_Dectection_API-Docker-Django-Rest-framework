from django.urls import path
from .views import AnomalyDetectionView

urlpatterns = [
    path("detect/", AnomalyDetectionView.as_view(), name="detect_anomaly"),
]
