What are we doing today
=======================
* Restaurant review website
* Playing with & modifying code
* This is meant to be interactive!
   * Keep your laptops on please =)


What is Django?
===============
* A MVC framework for websites
    * Traditionally it's Model, View, Controller
    * In Django it's MVT: Model, View, **Template**
 

How Does Data Move About
========================
* Browser --> Server --> *magic!* --> Django!
* let's ignore the magic, it's outside the scope of django anways


URLs and Back Again
===================
* URLS
* Views
    * Gather data
    * Send data to a template for rendering
* Back to the user, via *magic!*


Diving In: Starting Your Project
================================

.. code-block:: bash

    % django-admin.py startproject eatwell
    % cd eatwell
    % python manage.py runserver

* Point your browser to http://localhost:8000
* If you don't see "It worked!", flag one of us down.

--

* https://docs.djangoproject.com/en/1.4/intro/tutorial01/#creating-a-project


What's This Mess
================
You should have a file structure that looks a bit like this::

    eatwell/
      manage.py
      eatwell/
        __init__.py
        settings.py
        urls.py
        wsgi.py


So about those web pages...
===========================
* Remember urls --> views --> html
* Views return an HttpResponse, eventually.

* Hello World time.

--

* https://github.com/treyhunner/learning-django/commits/code-examples?page=1
  We'll be going through several commits here so be 
  ready for a light code dive.
  Go up to Add a new restaurants...

That only works...
==================
* If what your doing is very very small
* Python has classes, modules and libraries
* Django has classes, modules and...


Apps!
=====
* Created with `python manage.py startapp [appname]`
* Hint: Take a page from Unix. Do one thing, and do it well
   * look at the django.contrib stuff for examples

.. code-block:: bash
    # When in the eatwell/eatwell directory

    % python ../manage.py startapp restaurants

* App name == Project name -> failure
* Don't forget about your settings.py!

More Files
==========
Now it's been updated to look like::

    eatwell/
      manage.py
      eatwell/
      +  restaurants/
      +    __init__.py
      +    models.py
      +    tests.py
      +    views.py
        __init__.py
        settings.py
        urls.py
        wsgi.py




Get that HTML outta my code!
============================
* This is Django, not PHP
* Template Language
* Deliberately limited in what you can do


--

* https://docs.djangoproject.com/en/1.4/topics/templates/
* https://docs.djangoproject.com/en/1.4/ref/templates/builtins/

Working with templates
======================
* {% block %} and {% extends %}
* Passing data from views


Making it classy
================
* TemplateView
   * Code reuse
   * Composition with some inheritiance
* Lot of other SomethingViews, we'll cover some
  more today


