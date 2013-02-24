Django Packages
===============

A very informat presentation given by Trey Hunner at Django Day on 2013-02-23.

Presentation format: open up links below and explain why each package is cool.


Models and Database
-------------------

* [South][] for database migrations
* [Django model utils][] for some frequently useful model utilities/mixins

[south]: http://south.aeracode.org/
[django model utils]: https://github.com/carljm/django-model-utils


Views
-----

* [django braces][] for some generic class-based-view mixins
* [django extra views][] for more class-based-views
* [tastypie][] and [django rest framework][] are both good frameworks for creating RESTful APIs

[django braces]: http://django-braces.readthedocs.org/en/latest/index.html
[django extra views]: https://github.com/AndrewIngram/django-extra-views
[tastypie]: http://tastypieapi.org/
[django rest framework]: http://django-rest-framework.org/


Forms & Templates
-----------------

* [django widget tweaks][] for rendering form fields in a more customized way
* [django compressor][] for compressing CSS and JavaScript and precompiling SASS, less, CoffeeScript, etc.

[django widget tweaks]: https://bitbucket.org/kmike/django-widget-tweaks/
[django compressor]: https://github.com/jezdez/django_compressor


Miscellaneous/General
---------------------

* [django debug toolbar][] for debugging in your browser
* [django extensions][] is a kitchen sink of miscellaneous Django-related tools
* [sentry][] for logging/managing errors

[sentry]: https://github.com/getsentry/sentry
[django debug toolbar]: https://github.com/django-debug-toolbar/django-debug-toolbar
[django extensions]: http://pythonhosted.org/django-extensions/


Testing-Related
---------------

* [django discover runner][]
* [django hotrunner][]
* [mock][]
* [factory_boy][]
* [freezegun][]

[django discover runner]: https://github.com/jezdez/django-discover-runner
[django hotrunner]: https://bitbucket.org/metametrics/django-hotrunner
[factory_boy]: https://github.com/dnerdy/factory_boy
[freezegun]: https://github.com/spulec/freezegun
[mock]: http://www.voidspace.org.uk/python/mock/


Security
--------

* [django secure][]
* [django admin honeypot][]

[django secure]: https://github.com/carljm/django-secure
[django admin honeypot]: https://github.com/dmpayton/django-admin-honeypot
