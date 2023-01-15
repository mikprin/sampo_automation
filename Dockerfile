FROM python:3.9-slim

LABEL name="Sampo bot container" \
      version="1.0" \
      maintainer="Mikhail Solovyanov <" \
      description="This is the Dockerfile for t.me/how_was_your_day_miksolo_bot app"

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    software-properties-common \
    && rm -rf /var/lib/apt/lists/* &&\
    apt-get clean

COPY requirements.txt /app

COPY .env /

RUN pip3 install -r requirements.txt

COPY dance_sampo_bot /app


CMD ["python3", "bot.py"]