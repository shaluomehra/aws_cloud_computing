# Creating your own Base AMI

We have been using scripts to load up nGinx and the Sparta app everytime we want to use them, instead we can create our own AMI that will already have these deployed on there. First thing we're going to do is load our instance with nGinx installed and the Sparta App ready to be deployed: 
![Screenshot 2023-10-03 154927.png](images%2FScreenshot%202023-10-03%20154927.png)

Go into your AWS instance and click Actions:
![Screenshot 2023-10-03 155320.png](images%2FScreenshot%202023-10-03%20155320.png)

Select Image and templates and click the first option:
![Screenshot 2023-10-03 155435.png](images%2FScreenshot%202023-10-03%20155435.png)

Fill in the necessary details and then finally click create image:
![Screenshot 2023-10-03 155512.png](images%2FScreenshot%202023-10-03%20155512.png)

Now to use this AMI when creating an instance and selecting an AMI, first select My AMIs, then search for your AMI
![Screenshot 2023-10-03 155734.png](images%2FScreenshot%202023-10-03%20155734.png)

You will now have all the necessary installations ready when deploying the sparta app

## NOTE:
![Screenshot 2023-10-03 160601.png](images%2FScreenshot%202023-10-03%20160601.png)

We need to change the 'root' to 'ubuntu' when copying over to Git Bash




