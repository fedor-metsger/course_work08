
FROM python:3.9

ENV PYTHONUNBUFFERED=1

WORKDIR /src

COPY . .

RUN pip install -r requirements.txt

CMD ./manage.py migrate
