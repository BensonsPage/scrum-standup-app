"""Sign-up & log-in forms."""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import (
    Email,
    Length,
    DataRequired
)

class Request(FlaskForm):
    """Notes Submission Form."""
    note = StringField(
        'Note',
        validators=[
            Length(min=5),
            DataRequired()
        ]
    )
    email_address = StringField(
        'Email',
        validators=[
            Length(min=6),
            Email(message='Enter a valid email.'),
            DataRequired()
        ]
    )
    submit = SubmitField('Add Standup Notes')