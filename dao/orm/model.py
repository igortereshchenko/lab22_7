from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class ormGanre(Base):
    __tablename__ = 'orm_ganre'
    name = Column(String(15), primary_key=True)
    popularity = Column(Integer)
    count_of_subscribers = Column(Integer)
    year = Column(Integer)
    melody = relationship("ormMelody", back_populates="orm_ganre")

class ormMelody(Base):
    __tablename__ = 'orm_melody'
    melody_title = Column(String(15), primary_key=True)
    melody_singer = Column(String(15))
    melody_genre = Column(String(15), ForeignKey('orm_ganre.name'))
    orm_ganre = relationship("ormGanre", back_populates="melody")
