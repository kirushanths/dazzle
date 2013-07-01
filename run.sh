#!/bin/bash
sudo pip install -r requirements.txt
python ./dazzle/manage.py runserver [::]:8000
