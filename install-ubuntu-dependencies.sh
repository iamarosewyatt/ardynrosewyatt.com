#!/bin/bash

set -e

echo "Install Python 3+"
apt-get install python3 python3-pip python3-venv

echo "Install Apache 2+"
apt-get install apache2 apache2-dev libapache2-mod-wsgi-py3

echo "Install MySQL"
apt-get install mysql-server mysql-client libmysqlclient-dev
