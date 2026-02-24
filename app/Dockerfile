FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
<<<<<<< HEAD
RUN pip install pytest pytest-cov
=======
>>>>>>> a0036b4867e917ca07ce2b1c346e6c23f8d75649
COPY . .
EXPOSE 8443
CMD ["python","server.py"]