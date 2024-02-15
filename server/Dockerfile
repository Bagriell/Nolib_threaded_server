FROM python:3.10-slim

WORKDIR /server
ENV SERVER_HOST="192.20.0.5"
COPY . /server
EXPOSE 2111
CMD ["python", "main.py"]