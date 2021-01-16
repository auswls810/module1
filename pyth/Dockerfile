FROM python:3.7.9-alpine3.12

WORKDIR /usr/src
RUN pip install pymysql

COPY ./action.py ./
COPY ./first_form.py ./

CMD ["python", "first_form.py"]