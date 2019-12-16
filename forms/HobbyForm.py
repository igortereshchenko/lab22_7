from flask_wtf import Form, FlaskForm
from wtforms import StringField,   SubmitField,  PasswordField, DateField, HiddenField, IntegerField
from wtforms import validators

class HobbyForm(FlaskForm):
    id = HiddenField()

    name = StringField("Hobby name: ", [
        validators.DataRequired("Please enter a hobby name."),
        validators.Length(3, 15, "Value should be from 3 to 15 symbols")
    ])

    year = IntegerField("Year: ", [
        validators.number_range(2019, None, "Year should be from 2000 to 2019")
    ])

    tags = StringField("Hobby name: ", [
        validators.DataRequired("Please enter a hobby name.")
    ])

    rating = IntegerField("Rating: ", [
        validators.number_range(0, None, "Rating should be greater than 0")
    ])

    submit = SubmitField("Save")