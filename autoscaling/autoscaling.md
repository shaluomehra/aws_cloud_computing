# Creating Autoscaling instances
![Screenshot 2023-10-06 164711.png](images%2FScreenshot%202023-10-06%20164711.png)
### Step 1
We need to create an Auto Scaling Group, so navigate to the bottom on the left panel and click Auto Scaling Group then click 'Create Auto Scaling group'

![Screenshot 2023-10-06 151008.png](images%2FScreenshot%202023-10-06%20151008.png)

### Step 2
Give an appropriate name, just like below and we need to bring in the Template we created earlier then click 'Next'

![Screenshot 2023-10-06 151458.png](images%2FScreenshot%202023-10-06%20151458.png)

### Step 3
We need to define which availability zones our auto scaling group can use (we need to use the ones shown below)

![Screenshot 2023-10-06 152022.png](images%2FScreenshot%202023-10-06%20152022.png)

We can keep our Instance type requirements the same as this will be loaded from our Launch Template, click 'Next'

### Step 4

Creating a load balancer, we need to create a new load balancer and select 'Application Load Balancer' since we're dealing with HTTP (make sure to use an appropriate name), and we also need to change our load balancer scheme to 'Internet-facing' as shown below

![Screenshot 2023-10-06 153431.png](images%2FScreenshot%202023-10-06%20153431.png)

Next we need to create a new Target Group for our load balancer

![Screenshot 2023-10-06 153807.png](images%2FScreenshot%202023-10-06%20153807.png)

Next we need to turn on Load Balancing health checks and then we can click 'Next' and move on to Step 5

![Screenshot 2023-10-06 153912.png](images%2FScreenshot%202023-10-06%20153912.png)

### Step 5

Configuring group sizes and desired, min, max number of instances: <br>
We want a minimum of 2 instances created where it will run the app, and a maximum of 3 instances running IF the first two instances reach a certain capacity of usage

![Screenshot 2023-10-06 154812.png](images%2FScreenshot%202023-10-06%20154812.png)

Next we want a tracker to resize our autoscaling group when need be, in this case we have said if a CPU reaches 50% capacity it will create a new instance after that click 'Next'

![Screenshot 2023-10-06 155020.png](images%2FScreenshot%202023-10-06%20155020.png)

### Step 6

Here we have the option of sending a notification whenever the Auto Scaling Group launches or terminates <br>
We can skip this for now so click 'Next'

![Screenshot 2023-10-06 155220.png](images%2FScreenshot%202023-10-06%20155220.png)

### Step 7

Now we have the option to add a tag, **It's really important to add tags so the ASG has a name**, then click 'Next'

![Screenshot 2023-10-06 155753.png](images%2FScreenshot%202023-10-06%20155753.png)

Now we will be put on the review page, check each step to see if you have done it correctly and if so click 'Create Auto Scaling group'

### Step 8

Check our instances have been created we are expecting two instances to be running with the same name and the same functionality <br>
Navigate to your instances and we can see two instances in two **different** availability zones

![Screenshot 2023-10-06 160252.png](images%2FScreenshot%202023-10-06%20160252.png)

### Step 9

To test if our ASG works, we are going to forcefully terminate one of the instances and see what happens:

![Screenshot 2023-10-06 160600.png](images%2FScreenshot%202023-10-06%20160600.png)

After a couple minutes, the ASG will start another instance for us as shown below

![Screenshot 2023-10-06 161150.png](images%2FScreenshot%202023-10-06%20161150.png)










