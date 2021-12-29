FROM python:3.7.12-alpine

WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "src/app.py"]