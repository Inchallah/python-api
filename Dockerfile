FROM python:3.8-alpine
WORKDIR /app
RUN pip install flask
COPY . .
CMD [ "python", "app.py" ]