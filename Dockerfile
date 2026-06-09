# Base Python 3.11 image
FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set working directory inside container
WORKDIR /app

# Copy workspaces and configs
COPY .agents /app/.agents
COPY planner_workspace /app/planner_workspace
COPY build_workspace /app/build_workspace
COPY qa_workspace /app/qa_workspace

# Set Python path to include all workspaces
ENV PYTHONPATH="/app/build_workspace:/app/qa_workspace:${PYTHONPATH}"

# Default command: run pytest inside the QA workspace
CMD ["python", "-m", "unittest", "discover", "-s", "qa_workspace", "-p", "*_test.py"]
