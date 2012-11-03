Models
=======

All web applications have to store data. Most of them choose a database.

Typical Examples: MySQL, Postgres, Oracle DB, MongoDB, Redis

Defining Django Models
======================
Each django model is represented as a python class with special fields.

Example:

.. code-block:: python

    from django.db import models

    class Restaurant(models.Model):
        name = models.CharField(max_length=300)
        address1 = models.CharField(max_length=50)
        zip_code = models.CharField(max_length=10)


Quick Notes:
    * models.Model is a superclass
    * Possible options for a model
      - CharField
      - IntegerField
      - DateField
      - EmailField
      - BooleanFeild
      - few more
    

Taking to the Database from Django
==================================

syncDB - Creates the table based on the class definition.



Testing your Models
===================

Django Shell

  python manage.py shell



Django ORM
==========

ORM - Object Relation Mapper
Helps fetching data from the database.


all() - Returns all instances of a model. Example, returns all Restaurants. 

.. code-block:: python

    Employees.objects.all()


get() - Returns a single instance identified by an id. Example, returns ""

.. code-block:: python

    Employees.objects.get(10)



Creating the list of restaurants
================================

  
  


