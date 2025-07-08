FROM python:3.9-slim

# Create app user and switch to it
RUN useradd -m appuser
WORKDIR /home/appuser

# Install dependencies
COPY --chown=appuser:appuser requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy app files
COPY --chown=appuser:appuser main.py ./

# Switch to non-root user
USER appuser

# Run the service
EXPOSE 80
CMD ["python", "main.py"]
