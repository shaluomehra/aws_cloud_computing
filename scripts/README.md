# Writing a Script to deploy the app automatically

## Step 1
`#!/bin/bash`

This is called a shebang It is a special comment in the beginning of a script in Unix-like operating systems that tells the system what interpreter should be used to execute the script.

## Step 2
**We need to get these files or code onto our EC2 Instance**
```
git clone https://github.com/shaluomehra/sparta_test_app.git
```

## Step 3

**GO INTO THE DIRECTORY WHERE YOUR APPLICATION CODE IS LOCATED**

```
cd sparta_test_app
cd app
```
Make sure to go into the directory because this is where we need to install node.js and npm

## Step 4

**Set up the environment** <br>

We need to get an older version of node.js as our app is only compatible with this version

```
curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -
```

## Step 5

**Install node.js and npm**

```
sudo apt install nodejs -y
```

```
sudo npm install pm2 -g
```

```
sudo npm install
```

## Step 6

**Start the application**
```
node app.js
```
This will start the app on port 3000

## Step 7

We can now run this script, make sure to allow yourself to execute the code using:
```
chmod u+x app_provision.sh
```
