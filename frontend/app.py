from flask import Flask, jsonify, request, render_template, url_for, json
# import dbrequests
import mysql.connector
from datetime import date
from forms import Request
from os import environ

app = Flask(__name__)

# Get configs
app.config.from_object('config.DevelopmentConfig')
mydb = mysql.connector.connect(
    host= 'database',
    port= '3306',
    user= '',
    password= '',
    database= ''
    )

cursor = mydb.cursor(buffered=True)

# creating the date object of today's date
today_date = date.today()
current_year = str(today_date.year)

# Copyright
app_copyright = (" © " + current_year + " SCRUM Standup")


@app.route('/', methods=['GET', 'POST'])
def index():
    form = Request()

    if form.validate_on_submit():
        # getting user input, stand up note and email address/ name

        email_address = form.email_address.data
        note = form.note.data

        # Check if users exists and Add user if not
        mydb.reconnect()
        cursor.execute("SELECT user_id FROM users where email = %s", (email_address,))
        if cursor.fetchone() == "":
            cursor.execute("INSERT INTO users (email) VALUES(%s)", (email_address,))
            mydb.commit()
        cursor.execute("SELECT user_id FROM users where email = %s", (email_address,))
        user_id_q = cursor.fetchone()
        generated_user_id = user_id_q[0]

        # Insert a standup note.
        cursor.execute("INSERT INTO notes (user_id, note) VALUES (%s,%s)", (generated_user_id, note,))
        mydb.commit()

        #  Get Today's Standup Notes

    cursor.execute("SELECT note_id, note FROM notes where  DATE(created) = CURDATE();")
    notes = cursor.fetchall()

    return render_template(
        "index.html",
        form=form,
        notes=notes,
        app_copyright=app_copyright
    )

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html", app_copyright=app_copyright), 404

