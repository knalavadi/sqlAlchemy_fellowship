"""Models and database functions for cars db."""

from flask_sqlalchemy import SQLAlchemy

# Here's where we create the idea of our database. We're getting this through
# the Flask-SQLAlchemy library. On db, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)

db = SQLAlchemy()


##############################################################################
# Part 1: Compose ORM

class Model(db.Model):
    """Car model."""

    __tablename__ = "models"

    #renamed id to car_id since idis a reserved word 
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    year = db.Column(db.Integer, nullable=True)
    brand_name = db.Column(db.String(64), nullable=True) 
    name = db.Column(db.String(64), nullable=True) 

    def __repr__(self):
        return "<Model id=%s, year=%s, brand_name=%s, name=%s>" % (self.id, self.year, self.brand_name, self.name)



class Brand(db.Model):
    """Car brand."""

    __tablename__ = "brands"
    id = db.Column(db.Integer, db.ForeignKey('models.id'))
    name = db.Column(db.String, nullable=True)
    founded = db.Column(db.Integer, nullable=True) 
    headquarters = db.Column(db.String(64), nullable=True)
    discontinued = db.Column(db.Integer, nullable=True) 

    def __repr__(self):
        return "<Brand id=%s, name=%s, founded=%s, headquarters=%s, discontinued=%s>" % (self.id, self.name, self.founded, self.headquarters, self.discontinued)

#defines relationship to models 
    model = db.relationship("Model",
                        backref=db.backref("brands", order_by=id))


# End Part 1


##############################################################################
# Helper functions

def init_app():
    # So that we can use Flask-SQLAlchemy, we'll make a Flask app
    from flask import Flask
    app = Flask(__name__)

    connect_to_db(app)
    print "Connected to DB."


def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:///cars'
    app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    # So that we can use Flask-SQLAlchemy, we'll make a Flask app
    from flask import Flask

    app = Flask(__name__)

    connect_to_db(app)
    print "Connected to DB."
