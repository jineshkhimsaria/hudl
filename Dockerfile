FROM python:3.11.1-alpine3.17@sha256:4fc84c93c255afc1f83766d8b736ce2c8ca82f6489193cab709fcde759f720a2

# Install nodejs, npm, openssl, wget, bash, dpkg, xeyes
RUN pip install pipenv==2024.0.1
RUN apk update && \
    apk add curl nodejs npm openssl wget && \
    apk add --no-cache bash dpkg xeyes && \
    apk add chromium && \
    apk add chromium-chromedriver

# Download and unpack Chrome

# Set working directory, copy contents & install python libraries
WORKDIR /app
COPY . .
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy
ENV PYTHONPATH=/app/.venv/lib/python3.11/site-packages/:$PYTHONPATH

CMD ["python", "-m", "pytest", "hudl_test.py"]