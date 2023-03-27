FROM python:3.9.5-slim

RUN groupadd -r flask && useradd -r -g flask flask && \
    mkdir /src && \
    chown -R flask:flask /src

COPY ./ /src/fisher_book/

WORKDIR /src/fisher_book

RUN pip install -r requirements.txt

USER flask

ENV MYSQL_HOST=mysql

EXPOSE 5000

CMD ["python", "yushu.py"]