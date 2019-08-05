FROM python:3.7.3-slim-stretch
ENV PORT 8080
EXPOSE 8080
WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP "app.py"

ENTRYPOINT ["python"]
CMD ["app.py"]