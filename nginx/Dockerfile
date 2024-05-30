FROM nginx:1.19.5

RUN echo "nginx build start"

COPY ./nginx.conf /etc/nginx/nginx.conf

USER root

CMD ["nginx", "-g", "daemon off;"]
