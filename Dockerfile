FROM ubuntu:18.04

WORKDIR /app

RUN apt update
RUN apt install -y \
    python3 \
    gnupg2 \
    lsb-release \
    ca-certificates

RUN apt-key adv \
    --keyserver keyserver.ubuntu.com \
    --recv-keys 4052245BD4284CDD

RUN \
    echo "deb [trusted=yes] https://repo.iovisor.org/apt/$(lsb_release -cs) $(lsb_release -cs)-nightly main" | \
    tee /etc/apt/sources.list.d/iovisor.list

RUN apt update
RUN apt install -y \
    python3-bcc \
    bcc-tools \
    libbcc-examples

