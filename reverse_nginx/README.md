# NGINX Reverse Proxy

## What are ports?
Ports are communication endpoints that allow different services or applications to connect and communicate over a network. They are identified by a numerical value, ranging from 1 to 65535

## What is a reverse proxy? How is it different to a proxy
![Forward-proxy-vs-reverse-proxy-1.png](Forward-proxy-vs-reverse-proxy-1.png)

A forward proxy allows computers within a private network to access the public internet, whereas a reverse proxy enables computers on the internet to reach a private subnet <br>

## What is Nginx's default configuration?
The default configuration for NGINX is stored in the sites-available directory. It typically includes a default server block that listens on port 80.

## How to setup a Reverse NGINX Proxy

We're going to use our own AMI to do showcase this, this AMI has Nginx and the Sparta App already installed so if you haven't already get this done on your ec2 instance <br>

Open the configuration file in a text editor:
```
sudo nano /etc/nginx/sites-available/default
```

Next we need to setup the proxy pass, within the `server` block we need to specify we want the proxy to go so we remove 
```
try_files $uri $uri/ =404;
```
And we replace with a proxy pass which will specify the address
```
proxy_pass http://localhost:3000;
```
In this case our app is running on port 3000 and that's where we want to go <br>

Apply the new configuration by restarting Nginx:
```
sudo systemctl restart nginx
```
Now we need to run the app so first go into the folder containing the app and typing `app node.js` to start the application <br>

To test if the app will now show on just the ec2 ip address we can go to our web browser and paste in the public URL for our instance into the URL

![Screenshot 2023-10-04 115714.png](Screenshot%202023-10-04%20115714.png)

And Voila!
