import os
import time
import boto3
import pandas as pd
import mammoth
from datetime import datetime, timezone, timedelta
from pathlib import Path


AWS_ACCESS_KEY = "***********"
AWS_SECRET_KEY = "***********"
VERIFIED_AWS_MAIL = "***********"

# === Setup dynamic paths (Desktop) ===
desktop = Path.home() / "Desktop"
project_folder = desktop / "email_sender"
input_dir = project_folder / "input"
output_dir = project_folder / "output"
template_path = input_dir / "template.docx"
contacts_path = input_dir / "contacts-test.xlsx"
log_path = output_dir / "logs.csv"

# Ensure folders exist
os.makedirs(input_dir, exist_ok=True)
os.makedirs(output_dir, exist_ok=True)

# === Check if log file is locked (e.g. open in Excel) ===
def check_log_file_lock(path):
    if not os.path.exists(path):
        return True
    try:
        with open(path, 'a'):
            return True
    except PermissionError:
        return False

# === Convert Word to HTML using mammoth ===
def load_template_as_html(docx_path):
    with open(docx_path, "rb") as docx_file:
        result = mammoth.convert_to_html(docx_file)
        return result.value  # Clean HTML content

# === Replace placeholders like {managerName} with values from Excel ===
def personalize_template(html, data_row):
    message = html
    for col in data_row.index:
        placeholder = f"{{{col}}}"
        value = str(data_row[col])
        if placeholder in message:
            message = message.replace(placeholder, value)
    print(f"personalized_body {message}")
    return message

# === Send Email using Amazon SES ===
def send_email(to_email, subject, html_body):
    ses = boto3.client(
        'ses',
        region_name='us-east-1',  # ✅ Your AWS SES region
        aws_access_key_id=AWS_ACCESS_KEY,  # 🔐 Replace securely
        aws_secret_access_key=AWS_SECRET_KEY
    )

    response = ses.send_email(
        Source=VERIFIED_AWS_MAIL,  # ✅ Must be verified in SES
        Destination={'ToAddresses': [to_email]},
        Message={
            'Subject': {'Data': subject},
            'Body': {'Html': {'Data': html_body}}
        }
    )
    return response

# === Log result to CSV (KST time) ===
def log_result(email, status, message_id=None, error=None):
    korea_tz = timezone(timedelta(hours=9))
    now_kst = datetime.now(korea_tz)
    formatted_time = now_kst.strftime("%Y-%m-%d %H:%M:%S:%f")[:-3]

    log_entry = {
        "Timestamp": formatted_time,
        "Email": email,
        "Status": status,
        "MessageId": message_id or "",
        "Error": error or ""
    }

    try:
        log_df = pd.DataFrame([log_entry])
        if os.path.exists(log_path):
            log_df.to_csv(log_path, mode='a', header=False, index=False)
        else:
            log_df.to_csv(log_path, mode='w', header=True, index=False)
    except PermissionError:
        print("⚠️ Could not write to log file — it might be open in Excel.")

# === Main Function ===
def main():
    if not check_log_file_lock(log_path):
        print("🚫 Please close 'logs.csv' and run the program again.")
        return

    html_template = load_template_as_html(template_path)
    df = pd.read_excel(contacts_path)

    for _, row in df.iterrows():
        email = row['Email']
        personalized_body = personalize_template(html_template, row)

        try:
            response = send_email(email, "Your Offer from Our Company", personalized_body)
            message_id = response['MessageId']
            print(f"✅ Sent to {email} | Message ID: {message_id}")
            log_result(email, "Success", message_id=message_id)
        except Exception as e:
            print(f"❌ Failed to send to {email}: {e}")
            log_result(email, "Failed", error=str(e))

        time.sleep(0.1)  # Throttle: 10 emails/sec

if __name__ == "__main__":
    main()
