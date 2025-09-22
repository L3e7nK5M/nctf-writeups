FROM alpine:latest

RUN apk update && apk add --no-cache \
    lighttpd \
    php \
    php-cgi \
    php-session \
    php-mbstring \
    php-openssl
    #&& ln -sf /usr/bin/php-cgi /usr/bin/php-cgi

COPY lighttpd-reff.conf /etc/lighttpd/lighttpd.conf

# /root/referer を /var/www/htdocs/referer にマウント（run時指定）

#EXPOSE 8082

CMD ["lighttpd", "-D", "-f", "/etc/lighttpd/lighttpd.conf"]


