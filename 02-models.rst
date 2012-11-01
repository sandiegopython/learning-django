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
        name = forms.CharField()
        address = forms.CharField()
        city = forms.CharField()

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


all()

.. code-block:: python

    Employees.objects.all()


get()

.. code-block:: python

    Employees.objects.all()



Creating the list of restaurants
================================

Connecting the View and the models




