FROM python:3.12.3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/code

WORKDIR /code
COPY . /code

RUN pip install -r requirements.txt

CMD make dirhtml && perl -pi -e 's/document.body.dataset.theme = .*/document.body.dataset.theme = "light”;/' $(find _build/dirhtml -name '*.html')
