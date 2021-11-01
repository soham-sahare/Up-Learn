import email.message as em
import smtplib

import os

from flask import Flask, render_template, request, redirect, flash, session, Blueprint
from flask.helpers import url_for
from flask_login import login_required, current_user, login_user, logout_user

from datetime import timedelta
from itsdangerous import URLSafeTimedSerializer

from models import UserModel, ProjectsModel, db, login, CommentModel
from dotenv import load_dotenv

load_dotenv()

EMAIL_ADDRESS = os.environ.get("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")

def send_mail(TO, TOKEN):

    msgstr = "http://127.0.0.1:5000/authentication/reset/{}".format(TOKEN)

    msg = em.Message()
    msg['Subject'] = 'Password change request'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(msgstr)

    s = smtplib.SMTP("smtp.outlook.com", 587)
    s.starttls()

    s.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    s.sendmail(EMAIL_ADDRESS, TO, msg.as_string())
    s.quit()