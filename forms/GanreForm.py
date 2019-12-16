from flask_wtf import Form, FlaskForm
from wtforms import StringField,   SubmitField,  PasswordField, DateField, HiddenField, IntegerField
from wtforms import validators

class GanreForm(FlaskForm):
    id = HiddenField()

    genre_name = StringField("Ganre name: ", [
        validators.DataRequired("Please enter a ganre name."),
        validators.Length(3, 20, "Value should be from 3 to 20 symbols")
    ])

    genre_popularity = IntegerField("Popularity: ", [
        validators.number_range(0)
    ])

    genre_count_of_subscribers = IntegerField("Count of subscribers: ", [
        validators.number_range(0)
    ])

    genre_year = IntegerField("Year: ", [
        validators.number_range(2000, 2019, "Year should be from 2000 to 2019")
    ])

    submit = SubmitField("Save")