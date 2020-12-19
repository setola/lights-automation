FROM python:3.8-slim
WORKDIR /code
COPY requirements.txt .
COPY ./src .
RUN pip install -r requirements.txt

CMD [ "python", "-u", "./main.py" ]