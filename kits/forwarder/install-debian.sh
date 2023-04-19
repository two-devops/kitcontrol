#!/bin/bash
#
# Delfos Forwarder
# Compatible with Linux x64 SYSTEMD based systems

echo "\n-=[ Delfos Forwarder installation\n"

apt-get update && apt install -y curl sudo ntp apt-transport-https gnupg gnupg1 gnupg2

# Install td-agent from treasuredata and fluent-gem beats
curl -fsSL https://toolbelt.treasuredata.com/sh/install-debian-bullseye-td-agent4.sh | sh
/opt/td-agent/bin/fluent-gem install fluent-plugin-beats --no-document

# Set buffer directory
mkdir -p /opt/buffer && chmod 777 /opt/buffer

# Set config file
echo """
{% include 'td-agent.tpl' %}
""" > /etc/td-agent/td-agent.conf

# Enable and restart the service
systemctl enable td-agent && systemctl restart td-agent
