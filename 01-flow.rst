What is Django?
===============

* Django is a web application framework, written in python programming language
* Django helps you build a high quality web app
* A MVC framework 
    * Traditionally it's Model, View, Controller
    * In Django it's MVT: Model, View, **Template**
 

How Does Data Move About
========================
* Browser --> Server --> *magic!* --> Django!
* let's ignore the magic, it's outside the scope of django anyways


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

    % django-admin.py startproject pley
    % cd pley
    % python manage.py runserver

* Point your browser to http://localhost:8000
* If you don't see "It worked!", flag one of us down.

--

* https://docs.djangoproject.com/en/1.4/intro/tutorial01/#creating-a-project


What's This Mess
================
You should have a file structure that looks a bit like this::

    pley/
      manage.py
      pley/
        __init__.py
        settings.py
        urls.py
        wsgi.py

Apps
====
* Created with `python manage.py startapp [appname]`
* Hint: Take a page from Unix. Do one thing, and do it well

.. code-block:: bash

    % python manage.py startapp firstapp
