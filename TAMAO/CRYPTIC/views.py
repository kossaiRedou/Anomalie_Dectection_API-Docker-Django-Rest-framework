import pickle
import numpy as np
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import AnomalyDetection
from .serializers import AnomalyDetectionSerializer

# Charger le modèle d'Isolation Forest
model_path = "TAMAO/CRYPTIC/AI_Models/isolation_forest_model.pkl"
with open(model_path, "rb") as file:
    model = pickle.load(file)

class AnomalyDetectionView(APIView):
    def post(self, request):
        try:
            input_data = request.data.get("features")
            if not input_data:
                return Response({"error": "Missing 'features' field"}, status=status.HTTP_400_BAD_REQUEST)

            # Transformer les données en tableau numpy
            input_array = np.array(input_data).reshape(1, -1)

            # Faire la prédiction (1 = normal, -1 = anomalie)
            prediction = model.predict(input_array)[0] == -1

            # Sauvegarder dans la base de données
            anomaly = AnomalyDetection.objects.create(input_data=input_data, prediction=prediction)
            serializer = AnomalyDetectionSerializer(anomaly)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
