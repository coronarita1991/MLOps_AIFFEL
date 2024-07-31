FROM python:3.9-slim

RUN apt-get update && apt-get install -y \

    git \
    wget \
    && rm -rf /var/lib/apt/lists/*

RUN pip install -U pip &&\

    pip install boto3==1.26.8 mlflow==1.30.0 psycopg2-binary

RUN cd /tmp && \
    # MinIO에 초기 buckeet 생성 위한 MinIO Client설치
    wget https://dl.min.io/client/mc/release/linux-amd64/mc && \
    chmod +x mc && \
    mv mc /usr/bin/mc