FROM python:3.9-slim

# Install SQLite
RUN apt-get update && apt-get install -y sqlite3

# Set working directory
WORKDIR /data

# Copy initialization script
COPY init.sql /data/init.sql

# Expose SQLite files to a volume
VOLUME /data/db

# Initialize the database on first run
CMD ["sh", "-c", "sqlite3 /data/db/database.sqlite < /data/init.sql && tail -f /dev/null"]
