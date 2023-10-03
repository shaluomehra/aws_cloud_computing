# Connecting MongoDB with Sparta App

## Step 1
Create a new instance with our regular AMI (18.04 1e9) and create a new security group:
![Screenshot 2023-10-03 161314.png](images%2FScreenshot%202023-10-03%20161314.png)

Add a new security rule and input the Port Range 27017 which is the port for MongoDB
![Screenshot 2023-10-03 161406.png](images%2FScreenshot%202023-10-03%20161406.png)

## Step 2

Open a new GIT Bash Terminal and load up this instance on to it and then do your:
```
sudo apt update
```
and
```
sudo apt upgrade -y
```

## Step 3

Acquire the correct version of MongoDB since our application can only run with MongoDB v3.2, we need to use this line of code:
```
wget -qO - https://www.mongodb.org/static/pgp/server-3.2.asc | sudo apt-key add -
```

Next we need to get the key to this version using this code:
```
echo "deb http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list
```

Now we need to update our terminal again so use: 
```
sudo apt update
```

Now we install the MongoDB v 3.2 using this code:
```
sudo apt-get install -y mongodb-org=3.2.20 mongodb-org-server=3.2.20 mongodb-org-shell=3.2.20 mongodb-org-mongos=3.2.20 mongodb-org-tools=3.2.20
```
## Step 4

By default, MongoDB may bind to localhost (127.0.0.1) only, which means it won't accept remote connections. To allow remote connections, you need to modify the MongoDB configuration

We need to use the code: 
```
sudo nano /etc/mongod.conf
```
Find the bindIp configuration option and change it to bind to your server's IP address or 0.0.0.0 to listen on all network interfaces
```
bindIp: 0.0.0.0
```
## Step 5

Starting MongoDB, we need to now start MongoDB, use:
```
sudo systemctl start mongod
```
Then we need to enable it
```
sudo systemctl enable mongod
```
Just to check if its running and active we can use:
```
sudo systemctl status mongod
```
And if everything is fine we should get a screen like this:

![Screenshot 2023-10-03 164147.png](images%2FScreenshot%202023-10-03%20164147.png)

## Step 6

Now we need to connect the two instances (The App and the Database)
using environment variables

```
export DB_HOST=mongodb://54.229.176.98:27017/posts
```
Lets break this down: <br>
`export`: This is a command used in Unix-based systems to set or export environment variables. Environment variables are dynamic values that can affect the behavior of processes running in the system <br>

`DB_HOST`: This is the name of the environment variable being created or modified. In this case, it appears to represent the host (address) where a MongoDB server is running <br>

`mongodb://3.249.254.181:27017/posts`: This is the value being assigned to the DB_HOST environment variable. It follows a specific format: <br>

`27017`: This is the default port number used by MongoDB for client connections. MongoDB servers typically listen on port 27017

`/posts`: This part of the URI indicates the specific database or collection being accessed

Go into the directory where app.js is located then do:
```
npm install
```

Then finally run the program using:
```
node app.js
```

# Step 7

Paste our app URL into a web browser and stick in :3000 and /posts to see if its working <br>
In this instance our URL will be:
```
http://3.249.254.181:3000/posts
```

![Screenshot 2023-10-03 170420.png](images%2FScreenshot%202023-10-03%20170420.png)

And we've got it working!





