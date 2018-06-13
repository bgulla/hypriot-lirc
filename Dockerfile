FROM resin/rpi-raspbian
MAINTAINER <brandon@brandongulla.com>

RUN apt-get update; apt-get install -y inputlirc lirc python-dev  python-setuptools python-pip python-smbus python-rpi.gpio ; apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt


EXPOSE 8080

RUN mkdir /var/run/lirc
COPY ./src /app
RUN chmod +x /app/app.py

COPY ./supervisor/supervisor.conf /etc/supervisor.conf
COPY ./supervisor/lircd.conf /etc/supervisor/conf.d/lircd.conf
CMD ["supervisord","-c","/etc/supervisor.conf"]





