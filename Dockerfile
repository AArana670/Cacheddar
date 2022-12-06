FROM python:3.10-alpine

RUN apk -qq update
RUN pip install pymemcache.client

WORKDIR /app/src/

COPY cacheddar.py .

CMD python3 cacheddar.py
