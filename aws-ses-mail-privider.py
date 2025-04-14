import boto3
from botocore.exceptions import ClientError
AWS_ACCESS_KEY = "*********"
AWS_SECRET_KEY = "**********"
# === CONFIGURATION ===

# Sender (must be a verified email in SES)
SENDER = "KEFA Team <kefa@kefaknexus.com>"

# Region where your SES is set up
AWS_REGION = "*******"

# Email subject
SUBJECT = "Special Offer from KEFA Just for You!"

# Email encoding
CHARSET = "UTF-8"

# List of recipient emails (can be pulled from a CSV or DB later)
recipients = [
    "******.******@gmail.com.com",
    "otakhanov.*******.com",
    "knexus@********.com"
]

# Personalization data (optional)
recipient_data = {
    "******.********@gmail.com": "Ali",
    "********@gmail.com": "Askarjon",
    "********@ke-fa.com": "최원석"
}

# HTML template with placeholder
BODY_HTML_TEMPLATE = """
<html>
<head></head>
<body>
  <h2>Hello Dear {name},</h2>
  <p>We hope you're doing well!</p>
  <p>As a valued customer, we're excited to offer you an exclusive opportunity. 💡</p>
  <p><strong>Don't miss out!</strong></p>
  <br>
  <p>Best regards,<br>KEFA Team</p>
</body>
</html>
"""

# Plain-text fallback
BODY_TEXT_TEMPLATE = """
Hello {name},

We hope you're doing well!

As a valued customer, we're excited to offer you an exclusive opportunity.

Don't miss out!

- KEFA Team
"""

# === SES Client Initialization ===
client = boto3.client(
    'ses', 
    region_name=AWS_REGION,
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY)

# === Send Emails ===
for recipient in recipients:
    name = recipient_data.get(recipient, "Customer")

    body_html = BODY_HTML_TEMPLATE.format(name=name)
    body_text = BODY_TEXT_TEMPLATE.format(name=name)

    try:
        response = client.send_email(
            Source=SENDER,
            Destination={'ToAddresses': [recipient]},
            Message={
                'Subject': {
                    'Data': SUBJECT,
                    'Charset': CHARSET
                },
                'Body': {
                    'Text': {
                        'Data': body_text,
                        'Charset': CHARSET
                    },
                    'Html': {
                        'Data': body_html,
                        'Charset': CHARSET
                    }
                }
            },
            # Uncomment below if using SES Configuration Set
            # ConfigurationSetName='YourConfigSetName',
        )
        print(f"✅ Email sent to {recipient}. Message ID: {response['MessageId']}")
    except ClientError as e:
        print(f"❌ Failed to send to {recipient}: {e.response['Error']['Message']}")


# import boto3

# client = boto3.client(
#     'sts',
#     aws_access_key_id='********',
#     aws_secret_access_key='*************',
#     region_name='*********'
# )

# response = client.get_caller_identity()
# print(f"RES: {response}")
