# Install uv
FROM python:3.12-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Change the working directory to the `app` directory
WORKDIR /app

# Install dependencies
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --locked --no-install-project

# Install dependencies with uv
# COPY .python-version .
# COPY pyproject.toml .
# RUN uv sync --locked
# Copy application code
# COPY ./app/main.py ./
# COPY ./models/* ./models
# COPY ./routes/* ./routes
# COPY ./tests/* ./tests
# RUN ls -lrt
# RUN cat main.py
COPY . /app
# EXPOSE 8000

# CMD ["uv", "run","fastapi", "main.py", "--host", "0.0.0.0", "--port", "8000"]
