#!/bin/bash

#activate virtualenv
#cd /
#source ./venv/bin/activate
#dazzlevenv

#start server
sudo service nginx restart
sudo service uwsgi restart

cd /vagrant/src/
