FROM bash

WORKDIR /opt

# apk
RUN apk update && apk upgrade

# mysql
RUN apk add mysql-client && apk add mariadb-connector-c
# Connect: mysql -h mysql -u root

# psql
RUN apk add postgresql-client
# Connect: psql postgres://postgres:postgres@postgres:5432

# redis
RUN apk add redis
# Connect: redis -h redis -a redis

# kafka
ARG KAFKA_FILE=kafka_2.13-3.8.0.tgz
RUN wget https://dlcdn.apache.org/kafka/3.8.0/${KAFKA_FILE} && tar -xzf ${KAFKA_FILE} && rm ${KAFKA_FILE}

# Start and do nothing
CMD tail -f /dev/null