FROM amd64/python:3.9-slim

WORKDIR /usr/app

RUN pip install -U pip &&\

    pip install mlflow==1.30.0 pandas scikit-learn "fastapi[all]"

COPY schemas.py schemas.py
COPY app.py app.py
COPY sk_model/ sk_model/


# CMD ["uvicorn", "crud_pydantic:app", "--host", "0.0.0.0", "--reload"]
CMD ["python", "app.py"]