FROM mariadb:10-focal


COPY sql/init.sql /docker-entrypoint-initdb.d/init.sql

ENV MYSQL_ROOT_PASSWORD: root
ENV  MYSQL_USER: user
ENV  MYSQL_PASSWORD: password
ENV MARIADB_ROOT_PASSWORD: root

RUN apt-get update && apt-get -y install vim

EXPOSE 3306

CMD ["mysqld"]