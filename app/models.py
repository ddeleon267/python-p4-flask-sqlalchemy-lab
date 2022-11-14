from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Zookeeper(db.Model):
    __tablename__ = 'zookeepers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    birthday = db.Column(db.Date)
    animals = db.relationship('Animal', backref='zookeeper', lazy=True)

 #The Zookeeper model should contain a name, a birthday, and a list of animals that they take care of.

class Enclosure(db.Model):
    __tablename__ = 'enclosures'

    id = db.Column(db.Integer, primary_key=True)
    environment = db.Column(db.String)
    open_to_visitors = db.Column(db.Boolean)
    animals = db.relationship('Animal', backref='enclosure', lazy=True)

#The Enclosure model should contain an environment (grass, sand, or water), an open_to_visitors boolean, and a list of animals.
class Animal(db.Model):
    __tablename__ = 'animals'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    species = db.Column(db.String)
    zookeeper_id = db.Column(db.Integer, db.ForeignKey('zookeepers.id'),
        nullable=True)
    enclosure_id = db.Column(db.Integer, db.ForeignKey('enclosures.id'),
        nullable=True)
    # The Animal model should contain a name, a species, a zookeeper, and an enclosure.
