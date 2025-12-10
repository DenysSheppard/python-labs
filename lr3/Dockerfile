FROM python:3.12-slim

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir deep-translator

CMD ["python", "gtrans3.py"]