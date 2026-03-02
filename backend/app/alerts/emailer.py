import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def send_email(subject: str, content: str):
    message = Mail(
        from_email=os.getenv("ALERT_FROM_EMAIL"),
        to_emails=os.getenv("ALERT_TO_EMAIL"),
        subject=subject,
        plain_text_content=content,
    )

    try:
        sg = SendGridAPIClient(os.getenv("SENDGRID_API_KEY"))
        sg.send(message)
        return True
    except Exception as e:
        print(f"Email error: {e}")
        return False
