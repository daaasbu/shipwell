FROM python:3.7.3-slim-stretch
ENV PORT 8080
EXPOSE 8080
WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD exec gunicorn api.wsgi:application --bind 0.0.0.0:$PORT --workers 3
