from django.shortcuts import render
# detector/views.py
import cv2
from django.http import StreamingHttpResponse
from ultralytics import YOLO
import numpy as np
import os

# Cargar el modelo YOLOv8 entrenado. Asegúrate de que la ruta sea correcta.
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'models/best.pt')
model = YOLO(MODEL_PATH)

def gen_frames():
    # Abre la cámara (0 para la webcam)
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("No se pudo abrir la cámara")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Opcional: redimensiona el frame para mejorar el rendimiento (por ejemplo, 640x480)
        frame = cv2.resize(frame, (640, 480))

        # Ejecuta la detección con el modelo YOLOv8
        # La función model(frame) retorna una lista de resultados.
        results = model(frame)

        # Usar la función .plot() para obtener el frame anotado con las detecciones
        annotated_frame = results[0].plot()

        # Codificar el frame en JPEG
        ret2, buffer = cv2.imencode('.jpg', annotated_frame)
        if not ret2:
            continue

        frame_bytes = buffer.tobytes()

        # Genera el stream en formato MJPEG
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

    cap.release()

def video_feed(request):
    # StreamingHttpResponse envía el stream MJPEG al navegador.
    return StreamingHttpResponse(gen_frames(), content_type='multipart/x-mixed-replace; boundary=frame')

def index(request):
    return render(request, 'detector/index.html')