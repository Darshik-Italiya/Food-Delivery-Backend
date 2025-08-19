from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from pydantic import EmailStr
from dotenv import load_dotenv
import os

load_dotenv()

conf = ConnectionConfig(
    MAIL_USERNAME=os.getenv("MAIL_USERNAME"),
    MAIL_PASSWORD=os.getenv("MAIL_PASSWORD"),
    MAIL_FROM=os.getenv("MAIL_FROM"),
    MAIL_PORT=int(os.getenv("MAIL_PORT")),
    MAIL_SERVER=os.getenv("MAIL_SERVER"),
    MAIL_STARTTLS=os.getenv("MAIL_STARTTLS") == "True",
    MAIL_SSL_TLS=os.getenv("MAIL_SSL_TLS") == "True",
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True,
)


async def send_login_mail(email: EmailStr, name: str):

    message = MessageSchema(
        subject="Login Notification",
        recipients=[email],
        body=f"Hello {name}, you just logged in successfully!",
        subtype="plain",
    )

    fm = FastMail(conf)
    await fm.send_message(message)


async def send_register_mail(email: EmailStr, name: str):

    message = MessageSchema(
        subject="Register Notification",
        recipients=[email],
        body=f"Hello {name}, registered in successfully!",
        subtype="plain",
    )

    fm = FastMail(conf)
    await fm.send_message(message)
