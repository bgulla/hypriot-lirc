FROM resin/rpi-raspbian:jessie
MAINTAINER Brandon Gulla <im@brandongulla.com>

# Install dependencies
RUN apt-get update && apt-get install -y \
    python \
    python-dev \
    python-setuptools \
    python-virtualenv \
    inputlirc \
    lirc \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*


RUN easy_install Flask
RUN easy_install mimerender
RUN easy_install supervisor

EXPOSE 8080

RUN mkdir /var/run/lirc
COPY ./bin/app.py /app.py
RUN chmod +x /app.py

COPY ./supervisor/supervisor.conf /etc/supervisor.conf
COPY ./supervisor/lircd.conf /etc/supervisor/conf.d/lircd.conf
CMD ["supervisord","-c","/etc/supervisor.conf"]





