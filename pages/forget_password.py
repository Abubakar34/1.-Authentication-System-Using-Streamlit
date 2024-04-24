import streamlit as st
import smtplib
import csv
import random
from email.message import EmailMessage


# To Check if email registered or not
def is_email_register(email):
    with open("users.csv", "r") as file:
        reader = csv.reader(file)
        for user in reader:
            if user[2] == email:
                st.write("Register: True")
                return True
    return False


def send_email(receiver_email):

    temp_password = random.randint(10000, 99999)
    st.session_state["reset_password"] = str(temp_password)
    st.session_state["email"] = email

    smtp_server = "smtp.gmail.com"
    smtp_port = 465
    smtp_username = "Bakarali456@gmail.com"
    smtp_password = "ldkd pjxa taha ezji"

    sender_email = "Bakarali456@gmail.com"
    body = f"Reset Password: {temp_password}"
    subject = "Password Recovery Email"

    msg = EmailMessage()
    msg.set_content(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email

    server = smtplib.SMTP_SSL(smtp_server, smtp_port)
    server.login(smtp_username, smtp_password)
    server.send_message(msg)
    server.quit()


def generate_email(email):
    if is_email_register(email):
        st.success("Email Sent!")
        send_email(email)
    else:
        st.error("Please Creat an account first!")


with st.container():
    email = st.text_input(label="Email", placeholder="Enter your email")
    st.button("Get Password", on_click=generate_email, args=([email]))
