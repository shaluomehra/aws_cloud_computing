# Creating a New EC2 Instance on AWS

In this guide, we'll walk through the steps to create a new EC2 instance on AWS, paying special attention to Security Group settings, including IP Addresses and Ports. We'll also cover how to SSH into the instance and set up/deploy Nginx

## Step 1: Log into AWS Console

1. Go to [AWS Management Console](https://aws.amazon.com/console/)
2. Log in with your AWS account credentials

## Step 2: Launch New EC2 Instance

1. Navigate to the **EC2 Dashboard**
2. Click on the **"Launch Instance"** button

![Screenshot 2023-09-27 135352.png](images%2FScreenshot%202023-09-27%20135352.png)

## Step 3: Choose Amazon Machine Image (AMI)

1. Write a suitable name for the instance (following good practices of instance creation)
2. Select an AMI of your choice (e.g., Amazon Linux, Ubuntu, etc.) <br> In our case we are going to use a Community API (18.04 LTS Ubuntu)

![Screenshot 2023-09-27 135819.png](images%2FScreenshot%202023-09-27%20135819.png)

3. Choose an instance type in out case we are going to use t2.micro
4. You can use a key pair to securely connect to your instance. <br> Download the key pair in our case we have a tech_254 key pair (.pem file)

![Screenshot 2023-09-27 140415.png](images%2FScreenshot%202023-09-27%20140415.png)

5. Click **"Create a new security group"**
<br> Fill out the following information:

   - **Security group name:** "tech254_shaluo_basesg" (or a name of your choice)
   - **Description:** "tech254_shaluo_basesg" (or a desc of your choice)
![Screenshot 2023-09-27 141013.png](images%2FScreenshot%202023-09-27%20141013.png)
<br>


6. Inbound Security Group Rules:
- **Type:** SSH
- **Source:** Anywhere (For now, most like use your ip in the future)
- **Description:** Allow SSH traffic <br>

Click **"Add Rule"** to define new inbound rules:

- **Type:** HTTP
- **Source:** Anywhere (0.0.0.0/0 for public access)
- **Description:** Allow HTTP traffic <br> 


- **Type:** HTTPS
- **Source:** Anywhere (0.0.0.0/0 for public access)
- **Description:** Allow HTTPS traffic

7. Add Storage (Optional)

- Configure additional storage if required

8. Review and Launch your instance
![Screenshot 2023-09-27 142007.png](images%2FScreenshot%202023-09-27%20142007.png)

## Step 4: Accessing the EC2 Instance

1. Locate your newly created instance on the EC2 dashboard
2. Note down the **Public IPv4 address**

![Screenshot 2023-09-27 142424.png](images%2FScreenshot%202023-09-27%20142424.png)

## Step 5: SSH into the Instance

Open your Git Bash terminal or command prompt and navigate to the directory containing the .pem key file.
<br> Type in: 
```bash
chmod 400 tech254.pem
```
![Screenshot 2023-09-27 142813.png](images%2FScreenshot%202023-09-27%20142813.png)

<br> Next Type in:

```python
ssh -i "tech254.pem" ec2-user@<Public-IPv4-Address>
```
You can find the last part of that here:

![Screenshot 2023-09-27 143213.png](images%2FScreenshot%202023-09-27%20143213.png)

Your screen should look like this, type yes
![Screenshot 2023-09-27 143529.png](images%2FScreenshot%202023-09-27%20143529.png)

Next type these codes in 1 by 1 to update the system, install nginx and start it:

```python
sudo apt update -y
sudo apt install nginx -y
sudo service nginx start

```
## Step 6 Check if its working

Paste in the public ip address by going on your instance and pasting it onto the URL of a web browser

![Screenshot 2023-09-27 144528.png](images%2FScreenshot%202023-09-27%20144528.png)


