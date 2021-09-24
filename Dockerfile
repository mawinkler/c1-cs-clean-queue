FROM python:3.9.7-alpine3.14

RUN apk add --no-cache openssl-dev libffi-dev make build-base py3-pip bash && \
    apk del build-base libffi-dev openssl-dev

WORKDIR /app

# Install requirements
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt && \
    rm -f requirements.txt

# Copy in webhook listener script
COPY clean_queue.py ./clean_queue.py
CMD ["python3", "clean_queue.py"]
