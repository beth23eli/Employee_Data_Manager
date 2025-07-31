FROM python:3.10

WORKDIR /app

COPY requirements.txt .
RUN pip install cryptography
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

CMD ["python", "main.py"]
