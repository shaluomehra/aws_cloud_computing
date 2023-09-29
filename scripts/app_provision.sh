#!/bin/bash

# We need to get these files or code onto our EC2 Instance
git clone https://github.com/shaluomehra/sparta_test_app.git
#GO INTO THE DIRECTORY WHERE YOUR APPLICATION CODE IS LOCATED
cd sparta_test_app
cd app
# Set up the environment
curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -
# install node
sudo apt install nodejs -y
# install npm pm 2
sudo npm install pm2 -g
# install npm
sudo npm install
# start the application
node app.js

#./app_provision.sh to run the code