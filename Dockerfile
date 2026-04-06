# Stage 1: Builder
FROM python:3.12-slim as builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# Stage 2: Runner
FROM python:3.12-slim
WORKDIR /app
COPY --from=builder /install /usr/local
COPY . .

# Security: Run as non-root user
RUN useradd -m flaskuser
USER flaskuser

CMD ["flask", "run", "--host=0.0.0.0"]