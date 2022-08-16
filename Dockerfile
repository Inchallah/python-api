FROM python:3.8-alpine
WORKDIR /app
RUN pip install flask
COPY . .
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]