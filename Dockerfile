FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY app .

ENV PORT 8000
ENV HOST 0.0.0.0

CMD [ "sh", "-c", "streamlit run --server.port ${PORT} --server.address ${HOST} /app/main.py" ]