FROM python:3.12.3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/code

WORKDIR /code
COPY . /code

RUN pip install -r requirements.txt

CMD ["make", "dirhtml"]
