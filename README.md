# 🍅 TomateDetector

**TomateDetector** es una aplicación web desarrollada en **Django** que utiliza una red neuronal convolucional para detectar y clasificar tomates maduros e inmaduros mediante una cámara web en tiempo real.

---

## 📌 Descripción

Este proyecto combina visión por computadora con aprendizaje profundo para ofrecer una solución sencilla y eficaz a pequeños agricultores, productores o investigadores que necesiten clasificar tomates automáticamente.

---

## 📷 Características

- Detección en vivo desde cámara web
- Clasificación automática de tomates: `maduro` o `inmaduro`
- Interfaz web amigable
- API REST para envío de imágenes y predicción
- Entrenamiento personalizado del modelo (opcional)

---

## ⚙️ Requisitos

- Python ≥ 3.8  
- Django ≥ 3.2  
- OpenCV  
- PyTorch o TensorFlow (según el modelo entrenado)  
- Otros en `requirements.txt`

---

## 🚀 Instalación

```bash
# Clonar el repositorio
git clone https://github.com/Zitr-ctrl/TomateDetector.git
cd TomateDetector

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Migrar base de datos
python manage.py migrate

# Colocar el modelo entrenado en: media/models/model.pth

# Iniciar el servidor
python manage.py runserver
