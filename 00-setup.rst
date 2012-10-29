.. The goal of this section is to get Django installed
.. For users familiar with Python, Pip and Virtualenv,
.. this section will be entirely redundant.
.. By the end of this section, users should be ready
.. to start developing their own Django application.


Django Setup
============


Python Installation
===================

.. Not mentioning PATH issues on Windows in the slides
.. but this should be discussed live

* Download Python from `python.org <http://python.org/download>`_
* Django's latest release is for Python 2.7!
* Some command line familiarity is a must
* The `Python guide`_ (python-guide.org) is extremely helpful

.. _python guide: http://python-guide.org


Django Installation
===================

.. This is a presentation on Django (not Python) given with public Wifi
.. I don't want to spend the time explaining Pip or easy_install
.. and packages can't really be installed securely in this
.. setting anyway.

* Download Django from `djangoproject.com <https://djangoproject/download>`_
* Django is installed like other Python modules

  .. code-block:: bash

    % cd Django-1.4.2
    % python setup.py install
    % # On a Mac or Linux, you may need to run
    % sudo python setup.py install




Verifying Your Installation
===========================

.. code-block:: python

    % python
    >>> import django
    >>> print django.get_version()
    1.4.2
    >>> exit()
    % django-admin.py --help
    ...

Now you're ready to create a web site!

