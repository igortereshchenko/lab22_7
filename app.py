from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy.ext.declarative import declarative_base

from dao.db import PostgresDb
from dao import credentials
from dao.db import *

from forms.CountryForm import CountryForm
from forms.GanreForm import GanreForm

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, ForeignKey, func
from sqlalchemy.orm import relationship

from dao.orm.model import *
from dao.db import PostgresDb
from dao.credentials import *

db = PostgresDb()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "jkm-vsnej9l-vm9sqm3:lmve")

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL",
                                                  f"postgresql://{username}:{password}@{host}:{port}/{database}")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/g')
def insert_values():

    # session = db.sqlalchemy_session
    # # clear all tables in right order
    # session.query(ormGanre).delete()
    # session.query(ormMelody).delete()
    #
    # pop = ormGanre(name='pop', popularity=10000, count_of_subscribers=10000, year=2004)
    # indie = ormGanre(name='indie', popularity=10, count_of_subscribers=10, year=2007)
    # rock = ormGanre(name='rock', popularity=100, count_of_subscribers=100, year=2018)
    #
    # aaa = ormMelody(melody_title='AAA', melody_singer='Mur', melody_genre='indie')
    # haisfisch = ormMelody(melody_title='Haisfisch', melody_singer='Ramst', melody_genre='rock')
    # ccc = ormMelody(melody_title='CCC', melody_singer='Mur', melody_genre='indie')
    #
    # session.add_all([pop, indie, rock, aaa, haisfisch, ccc])

    # session.commit()
    return ("<h1>success!</h1>")

@app.route('/s', methods=['GET', 'POST'])
def show_values():
    result = db.sqlalchemy_session.query(ormGanre).all()
    return render_template('ganre.html', ganres=result)


# @app.route('/shop', methods=['GET', 'POST'])
# def show_country():
#     result = db.sqlalchemy_session.query(ormCountry).all()
#     return render_template('country.html', countries=result)

@app.route('/i', methods=['GET', 'POST'])
def new_ganre():
    form = GanreForm()
    db = PostgresDb()
    if request.method == 'POST':
        if not form.validate():
            return render_template('form_for_genre.html', form=form, form_name="New Ganre", action="i")
        else:
            genre_id = list(db.sqlalchemy_session.query(func.max(ormGanre.id)))[0][0]
            ganre_obj = ormGanre(
                id=genre_id+1,
                name=form.genre_name.data,
                popularity=form.genre_popularity.data,
                count_of_subscribers=form.genre_count_of_subscribers.data,
                year=form.genre_year.data)

            db.sqlalchemy_session.add(ganre_obj)
            db.sqlalchemy_session.commit()

            return redirect(url_for('show_values'))

    return render_template('form_for_genre.html', form=form, form_name="New Ganre", action='i')

# @app.route('/insert', methods=['GET', 'POST'])
# def new_country():
#     form = CountryForm()
#
#     if request.method == 'POST':
#         if not form.validate():
#             return render_template('form_for_country.html', form=form, form_name="New Country", action="insert")
#         else:
#             country_obj = ormCountry(
#                 name=form.country_name.data,
#                 population=form.country_population.data,
#                 goverment=form.country_goverment.data,
#                 location=form.country_location.data)
#
#             db.sqlalchemy_session.add(country_obj)
#             db.sqlalchemy_session.commit()
#
#             return redirect(url_for('show_country'))
#
#     return render_template('form_for_country.html', form=form, form_name="New Country", action="insert")

if __name__ == '__main__':
    app.run()
