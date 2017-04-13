#!/usr/bin/env bash
cp /vagrant/utility/docker-tcp.socket /etc/systemd/system/docker-tcp.socket
systemctl enable docker-tcp.socket
systemctl stop docker
systemctl start docker-tcp.socket
systemctl start docker
