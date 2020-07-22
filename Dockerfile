FROM nginx:alpine

# Change Nginx config here...
RUN rm /etc/nginx/conf.d/default.conf
ADD ./default.conf /etc/nginx/conf.d/
