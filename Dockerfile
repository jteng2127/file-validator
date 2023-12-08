FROM python:3.11.7-slim AS build

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN python setup.py sdist bdist_wheel

FROM python:3.11.7-slim

WORKDIR /data

COPY --from=build /app/dist/*.whl /app/

RUN pip install --no-cache-dir /app/*.whl

ENTRYPOINT ["file-validator"]