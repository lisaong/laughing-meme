# Docker for deploying: https://github.com/HackerShackOfficial/Smartphone-Doorlock

FROM resin/rpi-raspbian:stretch

RUN apt-get update \
    && apt-get install -y \
      build-essential \
      curl \
      gcc \
      git

RUN apt-get clean all && \
    rm -rf /var/lib/apt/lists/*

# node
RUN curl -sL https://deb.nodesource.com/setup_8.x -o /tmp/install_node.sh \
    && chmod +x /tmp/install_node.sh \
    && /tmp/install_node.sh \
    && apt-get install -y \
      nodejs \
      python-dev

# pigpio
WORKDIR /
RUN git clone https://github.com/joan2937/pigpio.git
WORKDIR /pigpio
RUN make \
    && make install

# project
WORKDIR /
RUN git clone https://github.com/lisaong/Smartphone-Doorlock.git
WORKDIR /Smartphone-Doorlock
RUN npm install
WORKDIR /

# tini
ENV TINI_VERSION v0.16.1
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini-armhf /usr/bin/tini
RUN chmod +x /usr/bin/tini

WORKDIR "/Smartphone-Doorlock"
ENTRYPOINT [ "/usr/bin/tini", "--" ]
CMD ["node", "doorlock.js"]