#!/bin/bash

# update
sudo apt update -y
# upgrade
sudo apt ugrade -y
# install nginx
sudo apt install nginx -y
# restart nginx
sudo systemctl restart nginx
# enable nginx
sudo systemctl enable nginx

#./provision to run the code

