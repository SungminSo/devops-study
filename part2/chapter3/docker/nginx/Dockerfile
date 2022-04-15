FROM nginx:latest

COPY auth_server/nginx/nginx.conf /etc/nginx/nginx.conf
COPY auth_server/nginx/nginx-app.conf /etc/nginx/sites-available/

RUN mkdir -p /etc/nginx/sites-enabled/\
    && ln -s /etc/nginx/sites-available/nginx-app.conf /etc/nginx/sites-enabled/ \

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
