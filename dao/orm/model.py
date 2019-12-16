
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, ForeignKey, Table
from sqlalchemy.orm import relationship

Base = declarative_base()
class ormGanre(Base):
    __tablename__ = 'orm_ganre'
    id=Column(Integer, primary_key=True)
    name = Column(String(15))
    popularity = Column(Integer)
    count_of_subscribers = Column(Integer)
    year = Column(Integer)
    melody = relationship("ormMelody", back_populates="orm_ganre")

class ormMelody(Base):
    __tablename__ = 'orm_melody'
    id=Column(Integer, primary_key=True)
    genre_id=Column(Integer, ForeignKey('orm_ganre.id'))
    melody_title = Column(String(15))
    melody_singer = Column(String(15))
    melody_genre = Column(String(15))
    orm_ganre = relationship("ormGanre", back_populates="melody")

class Student(Base):
    __tablename__='p_student'
    id = Column(Integer, primary_key=True)
    faculty = Column(String(20))
    group = Column(String(8))
    name = Column(String(15))
    surname = Column(String(15))
    username = Column(String(32))
    hobby = relationship("Hobby", back_populates="p_student")

class Hobby(Base):
    __tablename__='p_hobby'
    id = Column(Integer, primary_key=True)
    name = Column(String(15))
    year = Column(Integer)
    tags = Column(String(100))
    rating = Column(Integer)
    student_id = Column(Integer, ForeignKey('p_student.id'))
    p_student = relationship("Student", back_populates="hobby")
# association_table = Table('association', Base.metadata,
#     Column('ormperformer_id', String, ForeignKey('orm_performer.country')),
#     Column('ormcountry_id', String, ForeignKey('orm_country.name'))
# )
#
# class ormPerformer(Base):
#     __tablename__ = 'orm_performer'
#     name = Column(String(15), primary_key = True)
#     country = Column(String(15))
#     children = relationship("ormCountry",
#                     secondary=association_table,
#                             back_populates="parent")
#
# class ormCountry(Base):
#     __tablename__ = 'orm_country'
#     name = Column(String(15), primary_key = True)
#     population = Column(Integer)
#     goverment = Column(String(18))
#     location = Column(String(40))
#     parent = relationship("ormPerformer",
#                     secondary=association_table,
#                           back_populates="children")
