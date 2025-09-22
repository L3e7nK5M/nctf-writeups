FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y apache2 apache2-utils curl wget bash libcgi-fast-perl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN a2enmod cgid

RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf


RUN a2enconf serve-cgi-bin

COPY vuln.sh /usr/lib/cgi-bin/vuln.sh
COPY flag.txt /usr/lib/cgi-bin/flag.txt
RUN chmod +x /usr/lib/cgi-bin/vuln.sh /usr/lib/cgi-bin/flag.txt


COPY index.html /var/www/html/index.html
COPY diag.html /var/www/html/diag.html
COPY report.html /var/www/html/report.html
COPY admin.html /var/www/html/admin.html


RUN mkdir -p /tmp/hidden/access_denied/busted && \
    echo "NCTF{pR!vilE93_ESca1A7ION_Vu1neraB1117Y}" > /tmp/hidden/access_denied/busted/rootflag.txt && \
    chmod 600 /tmp/hidden/access_denied/busted/rootflag.txt

RUN apt-get update && apt-get install -y sudo && \
    echo "www-data ALL=(ALL) NOPASSWD: /usr/bin/cat" > /etc/sudoers.d/hint

EXPOSE 80

CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]

