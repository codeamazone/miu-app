FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /miu/
COPY requirements.txt /miu/
RUN pip install -r requirements.txt
COPY . /miu/