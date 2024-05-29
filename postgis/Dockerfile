FROM --platform=linux/amd64 postgis/postgis

ENV POSTGRES_DB=gpx
ENV POSTGRES_USER=root
ENV POSTGRES_PASSWORD=root

COPY ./init /docker-entrypoint-initdb.d

COPY ./data /data