from flask_wtf import Form, FlaskForm
from wtforms import StringField,   SubmitField,  PasswordField, DateField, HiddenField, IntegerField
from wtforms import validators

class CountryForm(FlaskForm):

    country_name = StringField("Country name: ", [
        validators.DataRequired("Please enter a country name."),
        validators.Length(3, 20, "Value should be from 3 to 20 symbols")
    ])

    country_population = IntegerField("Population: ", [
        validators.number_range(2)
    ])

    country_goverment = StringField("Type of goverment: ", [
        validators.any_of("унітарне", "демократичне")
    ])

    country_location = StringField("Location: ", [
        validators.Length(5, 20, "Value should be from 5 to 20 symbols")
    ])

    submit = SubmitField("Save")