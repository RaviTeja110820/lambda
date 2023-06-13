# EC2 Start Stop

The goal of this project is to automate the start and stop operations of Amazon EC2 instances at regular intervals using AWS lambda and CloudWatch Events. This automation helps optimize costs by ensuring that EC2 instances are only running when needed, such as during business hours.

## Steps

1. Create an IAM role: Start by creating an IAM role with the necessary permissions to manage EC2 instances. The role should have permissions to start and stop instances using the EC2 API. Note down the ARN (Amazon Resource Name) of the IAM role for later use.

	```json
	{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ec2:StartInstances",
                "ec2:StopInstances"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": "arn:aws:logs:*:*:*"
        }
    ]
}
,,,

2. Create a Lambda function: Create a new Lambda function in the AWS Management Console. Choose the appropriate runtime (e.g., Python 3.8) and configure the function with the IAM role created in step 1.

3. Write the Lambda function code: In the Lambda function code editor, write the code that checks the current time and starts or stops the EC2 instance accordingly. Use the code snippet provided earlier in this conversation as a starting point. Replace 'your_region_name' with the appropriate AWS region code and 'your_instance_id' with the actual ID of the EC2 instance you want to control.

4. Configure CloudWatch Events: In the AWS Management Console, go to the CloudWatch service. Create a new rule that triggers the Lambda function at the desired schedule (e.g., 9 AM and 6 PM daily). Specify the rule pattern or cron expression to define the schedule.

	* In the navigation pane, click on "Events" under the "Events" section.
	* Click on "Create rule" to create a new rule.
	* Under "Event Source", select "Schedule".
	* In the "Fixed rate of" section, enter 13 hours. This means the rule will trigger every 13 hours, starting from the time you create the rule.
	* In the "Cron expression" section, enter 0 9,18 * * ? *. This expression corresponds to triggering the rule at 9 AM and 6 PM every day.
	* The 0 represents the minute (0 minutes past the hour).
	* The 9,18 represents the hour (9 AM and 6 PM).
	* The * * ? * represents the rest of the fields for day-of-month, month, day-of-week, and year, allowing the rule to run every day.
	* Under "Targets", click on "Add target" and select your Lambda function from the dropdown list.
	* Configure any additional settings as needed.
	* Click on "Configure details".
	* Provide a name and description for the rule.
	* Review the settings and click on "Create rule" to save it.
	> CloudWatch Events will now trigger your Lambda function at 9 AM and 6 PM daily based on the specified cron expression.

5. Test and monitor: Test the setup by manually triggering the CloudWatch Events rule and verify that the Lambda function starts or stops the EC2 instance as expected. Monitor the CloudWatch Logs for the Lambda function to troubleshoot any issues and ensure that the function is executed correctly at the scheduled times.

By following these steps, you can set up an automated process using AWS Lambda and CloudWatch Events to start and stop an EC2 instance at specific times

![image](/Users/bodlaraviteja/repos/lambda/ec2StartStop/event.png)
