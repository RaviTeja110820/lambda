import boto3

def lambda_handler(event, context):
    # Connect to SES
    ses_client = boto3.client('ses')
    # Modify this line to use your actual list of email addresses
    recipient_list = ['lokeshanantha69@gmail.com']
    # Iterate through the list of recipients and send emails
    for recipient in recipient_list:
        email = {
            'Source': 'ravicandoitbetter@gmail.com',
            'Destination': {
                'ToAddresses': [
                    'lokeshanantha69@gmail.com'
                ]
            },
            'Message': {
                'Subject': {
                    'Data': 'Good Opportunity',
                    'Charset': 'UTF-8'
                },
                'Body': {
                    'Text': {
                        'Data': 'Antha seen ledu ley kani po iga',
                        'Charset': 'UTF-8'
                    }
                }
            }
        }

        # Send the email
        response = ses_client.send_email(**email)
        print('Email sent to:', recipient)
        print('Message ID:', response['MessageId'])

