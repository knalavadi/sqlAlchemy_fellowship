"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Part 2: Write queries

# 1.)
# Get the brand with the **id** of 8.
brand_id_8 = Brand.query.filter(Brand.id == 8).all()
print brand_id_8


# 2.)
# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
corvette_chevrolet_query = db.session.query(Model.name, Brand.name)
corvette_chevrolet = corvette_chevrolet_query.filter(Model.name=="Corvette", Brand.name=="Chevrolet")

# if corvette_chevrolet == (True, True)
# print corvette_chevrolet


# 3.)
# Get all models that are older than 1960.
older_1960_query = db.session.query(Model.year, Model.name)
older_1960 = older_1960_query.filter(Model.year<=1960)
print older_1960



# 4.)
# Get all brands that were founded after 1920.
founded_after_1920_query = db.session.query(Brand.name, Model.name)
founded_after_1920 = founded_after_1920_query.filter(Brand.founded>=1920)
print founded_after_1920


# 5.)
# Get all models with names that begin with "Cor".
name_Cor = Model.query.filter(Model.name.like('Cor%'))
print name_Cor


# 6.)
# Get all brands that were founded in 1903 and that are not yet discontinued.
founded1903_not_discontinued_query = db.session.query(Brand.name, Model.name)
founded1903_not_discontinued = founded1903_not_discontinued_query.filter(Brand.founded == 1903, Brand.discontinued == None)
print founded1903_not_discontinued

# 7.)
# Get all brands that are either 1) discontinued (at any time) or 2) founded 
# before 1950.
discontinued_or_founded1950_query = db.session.query(Brand.name, Model.name)
discontinued_or_founded1950 = discontinued_or_founded1950_query.filter((Brand.discontinued != None) | (Brand.founded <= 1960))
print discontinued_or_founded1950 


# 8.)
# Get any model whose brand_name is not Chevrolet.
name_not_chev = Model.query.filter(Brand.name.isnot('Chevrolet'))
print name_not_chev


# Fill in the following functions. (See directions for more info.)
print"hello"
def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''
    year = Brand.query.filter(Model.year == year).all()
    print year
print get_model_info(1960)


def get_brands_summary(brand):
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''
    brand = Brand.query.filter(Brand.name == name).all()
    print brand
print get_brands_summary('Cadillac')

#needs relationship in model.py
    

# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?
# 	a list of all the brands with a name of Ford. A list of objects 

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?


# -------------------------------------------------------------------
# Part 3

def search_brands_by_name(mystr):
    mystr = Brand.query.filter(Brand.name == mystr).all()


def get_models_between(start_year, end_year):
   start_year = Brand.query.filter(Brand.year == start_year).all()
   end_year = Brand.query.filter(Brand.year == end_year).all()

   diff_year = end_year - start_year







