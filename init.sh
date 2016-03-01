#!/bin/bash

sudo mkdir -p /home/box/web/public/{img,css,js}
sudo mkdir /home/box/web/{uploads,etc}

sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf

sudo nginx
