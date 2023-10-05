# Setting up an alarm system

First, go to the cloudwatch console page, from here, on the side panel click all alarms under the alarm section.

![Screenshot 2023-10-05 162745.png](images2%2FScreenshot%202023-10-05%20162745.png)

Next click 'Create Alarm'

![Screenshot 2023-10-05 162900.png](images2%2FScreenshot%202023-10-05%20162900.png)

And then 'Select Metric'

![Screenshot 2023-10-05 162918.png](images2%2FScreenshot%202023-10-05%20162918.png)

Copy and Paste your instance i.d into the search bar

![Screenshot 2023-10-05 163104.png](images2%2FScreenshot%202023-10-05%20163104.png)

Select 'EC2 > Per Instance'

![Screenshot 2023-10-05 163158.png](images2%2FScreenshot%202023-10-05%20163158.png)

Find the one with 'CPUUtilization' and click 'Select Metric'

![Screenshot 2023-10-05 163219.png](images2%2FScreenshot%202023-10-05%20163219.png)

Under Conditions, we want to get a notification when the CPU Usage is greater than 10%

![Screenshot 2023-10-05 163450.png](images2%2FScreenshot%202023-10-05%20163450.png)

We're going to create a new topic and put in our email so we get a notification when the CPU Usage is over 10%

![Screenshot 2023-10-05 163618.png](images2%2FScreenshot%202023-10-05%20163618.png)

Click 'Next' and 'Next' again, now you're alarm is ready, and when your CPU Usage is over 10% you will get an email like this: 

![Screenshot 2023-10-05 162242.png](images2%2FScreenshot%202023-10-05%20162242.png)


