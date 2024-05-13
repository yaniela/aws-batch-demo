# Usar una imagen base de Python oficial
FROM python:3.11-slim


# Copiar los requerimientos y el script a la imagen
COPY requirements.txt .
COPY sumar.py .


# Instalar las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Establecer el entrypoint
ENTRYPOINT ["python", "sumar.py"]
