FROM python:3.11-alpine

# Create non-root user
RUN addgroup -g 1001 -S appgroup && \
    adduser -u 1001 -S appuser -G appgroup

WORKDIR /app

# Copy application
COPY app.py .

# Change ownership to non-root user
RUN chown -R appuser:appgroup /app && \
    chmod 755 /app/app.py

# Document that the application listens on port 8080
EXPOSE 8080

# Switch to non-root user
USER appuser

# Health check
HEALTHCHECK --interval=10s --timeout=5s --start-period=10s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8080/')" || exit 1

# Run the application
CMD ["python", "-u", "app.py"]