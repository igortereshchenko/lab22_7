from dao.orm.model import *
from dao.db import PostgresDb

db = PostgresDb()


Base.metadata.create_all(db.sqlalchemy_engine)


session = db.sqlalchemy_session
# clear all tables in right order
session.query(ormGanre).delete()
session.query(ormMelody).delete()

pop = ormGanre(name = 'pop', popularity = 10000, count_of_subscribers = 10000, year = 2004)
indie = ormGanre(name = 'indie', popularity = 10, count_of_subscribers = 10, year = 2007)
rock = ormGanre(name = 'rock', popularity = 100, count_of_subscribers = 100, year = 2018)

aaa = ormMelody(melody_title = 'AAA', melody_singer = 'Mur', melody_genre = 'indie')
haisfisch = ormMelody(melody_title = 'Haisfisch', melody_singer = 'Ramst', melody_genre = 'rock')
ccc = ormMelody(melody_title = 'CCC', melody_singer = 'Mur', melody_genre = 'indie')

session.add_all([pop, indie, rock, aaa, haisfisch, ccc])

session.commit()