FROM python:3.8.2-slim

WORKDIR /usr/app/src

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY src ./

CMD ["sh", "-c", "streamlit run --server.port $PORT /usr/app/src/main.py"]