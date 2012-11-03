Learning Django
===============

Learning Django is a series of training materials originally created for the
`San Diego Python Users Group`_ loosely based off of the `Django tutorials`_

.. _San Diego Python Users Group: http://pythonsd.org
.. _Django tutorials: https://docs.djangoproject.com/en/1.4/intro/tutorial01/


Overview
--------

Learning Django takes students step-by-step through the creation of a
very simple restaurant review website in order to illustrate some of the
features of Django such as the following:

* Model-view-controller
* Getting started
* Querysets
* Forms & validation
* Class-based views
* Admin
* Debugging Django applications


Code companion
--------------

In addition, Learning Django provides the restaurant review site code.
After going through the slides, students are supposed to download the
code and show off their newly acquired skills by adding features to
the restaurant review application. Some suggestions for features include:

* Add a phone number field to restaurants
* Add the ability to search for restaurants by zip code
* Rewrite CreateReviewView to use django.views.generic.edit.CreateView
* Add a 1-5 star rating system for reviews and calculate average


Generating slides
-----------------

* Make sure you have the prerequisites

  ::

    % pip install -r requirements.txt

* Create the presentations

  ::

    % make

