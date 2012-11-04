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


Stepping through the code
-------------------------

The evolution of the eatwell project may be viewed in a step-by-step fashion
using git or a graphical git tool (such as the Github website).  All commits
are on the eatwell branch and may be viewed via git tags.  The tags are labeled
``s01`` through ``s37``.

Stepping through the project on Github
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The best way to walk through the code on the Github website is to go to commit
page for the `eatwell`_ branch and walk through the commits.  To walk through
the commits scroll down to the bottom of the page and click the "Older" button
until you are at the first commit.

Clicking on the "..." button next to a commit title will expand the commit
message, providing more details about the change and links to relevant
documentation pages.  Clicking on the commit message will show a diff of the
actual code changed (which shows lines added and removed).  From the diff pages
the files that were changed may be viewed individually by clicking the "View
file at ..." buttons.

.. _eatwell: https://github.com/pythonsd/learning-django/commits/eatwell

Stepping through the code in git
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have a git client on your machine it is easiest to walk through the code step-by-step using git.  Every commit in the eatwell branch has a tag associated with it.  The first commit has the tag ``s01``, the second ``s02``, the third ``s03`` and so on.

Cloning the code::

    git clone git://github.com/pythonsd/learning-django.git

Checking out the first step::

    git checkout s01

Checking out the next step::

    git checkout s02

If you change some files while experimenting with the code, to reset all of your changes to a particular step (``s01`` in this case) use the following command::

    git reset --hard s01


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

