# Deploying a Node.js App on AWS EC2

In this guide, we'll walk through the steps to deploy a Node.js application on an AWS EC2 instance. This assumes you have an AWS account and have already launched and connected (with SSH) to your EC2 instance. If you haven't please read the How To Start EC2 Instance markdown


## Step 1: Download the necessary application:

Download the application files you are going to need to load using Node.js, in this case we have downloaded the 'Sparta Global App' files

## Step 2: Transfer files to your EC2 Instance

We need to get these files or code onto our EC2 Instance to do this we can use two methods: <br>
- Using `scp` (Secure Copy Protocol): You can use the `scp` command to securely copy files between your local machine and an EC2 instance for example: <br>
```
scp -i <path-to-key-file> <local-file-or-directory> ec2-user@<public-ipv4-address>:<destination-path-on-instance>

For example:

scp -i "C:/Users/shaluo/.ssh/tech254.pem" -r app ubuntu@ec2-34-242-237-25.eu-west-1.compute.amazonaws.com:~
```
- Using Git:
   - Clone from a Public Repository: If your code is in a public Git repository (like on GitHub), you can use the git clone command to clone the repository directly onto your EC2 instance for example:
```
git clone <repo-url>

for example:

git clone https://github.com/LSF970/sparta_test_app.git
```

Your screen should look something like this once you `ls` to check the files: <br>

![Screenshot 2023-09-28 160516.png](images%2FScreenshot%202023-09-28%20160516.png)

## Step 3: Set Up the Environment

**GO INTO THE DIRECTORY WHERE YOUR APPLICATION CODE IS LOCATED**

### Install Node.js and npm

- NOTE: We are going to be using an older version of Node.js since our application is only compatible with that version

To tell our process which version we want we use this code: 
```
curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -
```
![Screenshot 2023-09-28 161048.png](images%2FScreenshot%202023-09-28%20161048.png)

**Wait for it to unpack this version of Node.js, skip this step if you want to use the latest version of Node.js** <br>

Next we install Node.js and npm:

```
sudo apt install nodejs -y
```
Check the version of Node.js using `node -v`

![Screenshot 2023-09-28 161927.png](images%2FScreenshot%202023-09-28%20161927.png)

Once this is complete install npm:
```
sudo npm install pm2 -g
```
Next do:
```
npm install
```

## Step 4: Start the application

To start the application simply write:
```
node app.js
```
Your Git Bash will print: 

![Screenshot 2023-09-28 162853.png](images%2FScreenshot%202023-09-28%20162853.png)

## Step 5: Adding the Port to our Security

- Go back the Instance Settings on AWS and navigate to your security <br>
- Click Edit Inbound Rules

![Screenshot 2023-09-28 163112.png](images%2FScreenshot%202023-09-28%20163112.png)

- Add a new rule that will allow our port to be connected to the Instance and click save

![Screenshot 2023-09-28 163227.png](images%2FScreenshot%202023-09-28%20163227.png)

- Add the port (3000) to the end of our URL (Public I.P)

![Screenshot 2023-09-28 163718.png](images%2FScreenshot%202023-09-28%20163718.png)

## Welcome to the Sparta Test App

![Screenshot 2023-09-28 163825.png](images%2FScreenshot%202023-09-28%20163825.png)
