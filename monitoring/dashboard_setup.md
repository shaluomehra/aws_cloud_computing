# How to Setup a Dashboard on AWS


We're going to create a new instance with a custom AMI which will start the app, I'm going to use Luke's nrp_ami_test which he created earlier as I don't have mine setup yet:

![Screenshot 2023-10-05 153355.png](images%2FScreenshot%202023-10-05%20153355.png)

Before we launch our instance we are going to scroll down and open 'Additional Details' and scroll till we find 'User Data' here we can input some code to run the Sparta App

```
#!/bin/bash

#we are user root so we need to tell git bash to go into ubuntu first and then where the app is located
cd/home/ubuntu/repo/app

sudo systemctl restartnginx
npm install
pm2 start app.js
```
![Screenshot 2023-10-05 151449.png](images%2FScreenshot%202023-10-05%20151449.png)

**Launch the instance and the app should run on your Public I.P**

To get the dashboard, first we need to click on our instance i.d, scroll and click the 'Monitoring' tab and next click 'Manage detailed monitoring'

![Screenshot 2023-10-05 154251.png](images%2FScreenshot%202023-10-05%20154251.png)

You'll get a screen like this, click 'enable' and 'confirm'

![Screenshot 2023-10-05 154442.png](images%2FScreenshot%202023-10-05%20154442.png)

Next to create the dashboard click 'Add to Dashboard'

![Screenshot 2023-10-05 154601.png](images%2FScreenshot%202023-10-05%20154601.png)

And then you'll get a screen like this, click 'Create new'

![Screenshot 2023-10-05 154617.png](images%2FScreenshot%202023-10-05%20154617.png)

Give it an appropriate name and click 'Create'

![Screenshot 2023-10-05 154916.png](images%2FScreenshot%202023-10-05%20154916.png)

And then click 'Add to Dashboard'

![Screenshot 2023-10-05 154926.png](images%2FScreenshot%202023-10-05%20154926.png)

And voila! you've created your dashboard!

![Screenshot 2023-10-05 155107.png](images%2FScreenshot%202023-10-05%20155107.png)













