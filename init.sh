#!/bin/bash

sudo mkdir -p /home/box/web/public/{img,css,js}
sudo mkdir /home/box/web/{uploads,etc}

sudo touch  /home/box/web/public/js/test.js
sudo rm  /etc/nginx/sites-enabled/default
sudo ln -s /home/box/stepic_webtech1/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo ln -s /home/box/stepic_webtech1/web/etc/hello.py  /etc/gunicorn.d/hello.py
sudo ln -s /home/box/stepic_webtech1/web/etc/ask.py    /etc/gunicorn.d/ask.py
sudo ln -s /home/box/stepic_webtech1/web/ask   /home/box/web/
sudo ln -s /home/box/stepic_webtech1/web/hello.py   /home/box/web/

#cd /home/box/stepic_webtech1/web
#gunicorn -c /etc/gunicorn.d/hello.py hello:app&

#cd /home/box/stepic_webtech1/web/ask/ask
#gunicorn -c /etc/gunicorn.d/ask.py wsgi:application&


sudo /etc/init.d/mysql start
sudo mysql -uroot -e "create database ask"
python /home/box/stepic_webtech1/web/ask/manage.py syncdb --noinput


sudo /etc/init.d/gunicorn start

sudo nginx
