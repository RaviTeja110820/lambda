import boto3

def lambda_handler(event, context):
    # Create an S3 client
    s3_client = boto3.client('s3')
    
    # Define the bucket name
    bucket_name = 'raviteja1108989898s'
    
    s3_client.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': 'ap-south-1'
        }
    )

    
    # Define file contents
    file1_content = 'This is the content of file 1'
    file2_content = 'This is the content of file 2'
    
    # Upload files to the bucket
    files_to_upload = [
        {'file_name': 'file1.txt', 'content': file1_content},
        {'file_name': 'file2.txt', 'content': file2_content}
    ]  # Replace with your desired file names and contents
    
    for file_info in files_to_upload:
        file_name = file_info['file_name']
        content = file_info['content']
        
        s3_client.put_object(
            Bucket=bucket_name,
            Key=file_name,
            Body=content.encode('utf-8')
        )
    
    # Enable block public access
    s3_client.put_public_access_block(
        Bucket=bucket_name,
        PublicAccessBlockConfiguration={
            'BlockPublicAcls': True,
            'IgnorePublicAcls': True,
            'BlockPublicPolicy': True,
            'RestrictPublicBuckets': True
        }
    )
    
    return {
        'statusCode': 200,
        'body': 'S3 bucket created and files uploaded successfully.'
    }
