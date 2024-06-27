# Use the official Python image from the Docker Hub
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Install Poetry
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python3 -

# Add Poetry to PATH
ENV PATH="/root/.local/bin:${PATH}"

# Copy the pyproject.toml and poetry.lock files to the container
COPY backend/pyproject.toml backend/poetry.lock ./

# Install dependencies
RUN poetry install --no-root

# Copy the rest of the application code to the container
COPY backend/ .

# Copy the create_fortune_history_table.py script to the container
COPY create_fortune_history_table.py .

# Expose the port the app runs on
EXPOSE 8000

# Run the application and create the fortune_history table
CMD ["sh", "-c", "poetry run python create_fortune_history_table.py && poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000"]
