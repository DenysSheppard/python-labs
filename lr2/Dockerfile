FROM python:3.12-slim

WORKDIR /Postument

COPY docker_translate.py .

RUN pip install googletrans==3.1.0a0

CMD ["python", "docker_translate.py"]