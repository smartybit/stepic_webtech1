#!/bin/bash

sudo mkdir -p /home/box/web/public/{img,css,js}
sudo mkdir /home/box/web/{uploads,etc}

sudo touch  /home/box/web/public/js/test.js
sudo rm  /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf

sudo nginx
