Eatwell Project
===============

Eatwell is a site containing information about restaurants and user-submitted
reviews of restaurants.  This project was made live on February 23, 2013 during
Django Day in San Diego.

This project is based on the EatWell project created for the November 3, 2012
Python SD Django Workshop.


Getting it Working
------------------

First you'll need a database.  Create the database file and database tables::

    ./manage.py syncdb

Then you can run the Django development server::

    ./manage.py runserver

Then visit http://127.0.0.1:8000/ in your web browser.
