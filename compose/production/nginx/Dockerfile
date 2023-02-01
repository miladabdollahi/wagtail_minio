FROM hub.hamdocker.ir/library/nginx:1.20.1

WORKDIR /project
ADD . .

RUN rm /etc/nginx/conf.d/default.conf
COPY ./compose/production/nginx/sites-enabled/mesbah.conf /etc/nginx/conf.d/default.conf
