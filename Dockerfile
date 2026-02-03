FROM nikolaik/python-nodejs:python3.11-nodejs20


RUN apt-get update && apt-get install -y --no-install-recommends \
    ffmpeg \
    build-essential \
    python3-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*


COPY requirements.txt /app/
WORKDIR /app/
RUN pip3 install --no-cache-dir -U -r requirements.txt
COPY . /app/

CMD bash start
