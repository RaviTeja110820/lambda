# S3 Bucket Files Upload

In this project, our goal is to utilize AWS Lambda to create an S3 bucket and upload files into it.

## Steps

1. role for the Lambda function
2. Configure the Lambda function
3. Test the Lambda function

## Setup

### Create Role for the Lambda function

1. Open the IAM console.
2. Navigate to "Roles" and click on "Create role".
3. Select "Lambda" as the service and choose the appropriate use case.
4. Assign the necessary permissions to the role, either by selecting an existing policy or creating a custom policy.
5. Add any optional tags and review the role details before creating it.

### Configure the Lambda Function

1. Open the AWS Management Console and navigate to the Lambda service.

2. Click on the "Create function" button to create a new Lambda function.

3. Choose the option to create a function from scratch.

4. In the "Function name" field, enter a name for your function (e.g., "s3-upload-function").

5. Select the desired runtime. In this case, choose "Python 3.8" or a newer version.

6. Under "Permissions," choose an existing or create a new execution role that has the necessary permissions to access S3. If you need to create a new role, follow the prompts to set up the required permissions.

7. Click on the "Create function" button to create the Lambda function.

8. In the function editor page, scroll down to the code editor section and replace the existing code with the provided code.

9. Scroll up to the "Basic settings" section and adjust the "Timeout" value as per your requirements. For example, you can set it to 5 minutes (300 seconds).

10. Click the "Save" button to save your Lambda function.

### Test the Lambda Function

1. test the Lambda function by clicking on the "Test" button located above the code editor.

2. Create a new test event by clicking on the dropdown next to the "Test" button and selecting "Configure test events." Enter a name for the test event (e.g., "s3-upload-test") and click on the "Create" button.

3. In the test event editor, you can leave the default event template or modify it as per your requirements. Click on the "Create" button to save the test event.

4. Finally, click on the "Test" button to execute the Lambda function with the test event.

5. You will see the execution result in the "Execution result" section, and if everything is successful, you should receive a response indicating that the S3 bucket was created and files were uploaded successfully.

>> Please note that you may need to adjust the bucket name, region, and file contents in the code to match your requirements.