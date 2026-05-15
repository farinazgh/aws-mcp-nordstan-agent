FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN pip install uv && uv sync --frozen --no-dev

COPY server.py .

ENV RESTAURANT_FUNCTION_NAME=nordstan-lambda
ENV AWS_DEFAULT_REGION=eu-west-1

ENV HOST=0.0.0.0
ENV PORT=8000

EXPOSE 8000

CMD ["uv", "run", "python", "server.py"]