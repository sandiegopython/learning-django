.. At this point students are familiar with models, views and urls
.. and they have seen the briefest bit of templates
.. Students haven't done anything that takes user input

Django Forms
============

.. Django forms validate input, have "widgets", etc.

* Forms are a way to take input from users of your application
* Django forms are a helper for creating HTML forms
* By convention, forms in Django live in a file ``forms.py``

What do forms look like
=======================

.. code-block:: python

    from django import forms

    class RestaurantForm(forms.Form):
        name = forms.CharField()
        address1 = forms.CharField()
        address2 = forms.CharField()
        city = forms.CharField()
        state = forms.CharField()
        zip_code = forms.IntegerField()


Wiring it up
============

.. Briefly mention GET and POST requests
.. Discuss the three code paths through this code
.. Show an error so they can see validation in action

.. code-block:: python

    from django.shortcuts import render
    from django.http import HttpResponseRedirect
    from .models import Restaurant
    
    def add_restaurant(request):
        if request.method == 'POST': # If the form has been submitted...
            form = RestaurantForm(request.POST) # A form bound to the POST data
            if form.is_valid(): # All validation rules pass
                # Process the data in form.cleaned_data
                # Save a new restaurant
                return HttpResponseRedirect('/thanks/') # Redirect after POST
        else:
            form = RestaurantForm() # An unbound form
    
        return render(request, 'contact.html', {
            'form': form,
        })


Wiring it up part two
=====================

.. Don't go into detail on CSRF other than it is a Django security feature

.. code-block:: html

    <form action="{% url restaurants.views.add_restaurant %}" method="post">
      {% csrf_token %}
      {{ form.as_p }}
      <input type="submit" value="Submit" />
    </form>


There's a shortcut! Model forms
===============================

.. code-block:: python

    from django import forms
    from .models import Restaurant

    class RestaurantForm(forms.ModelForm):
        class Meta:
            model = Restaurant

Model form advantages
=====================

* Create a form based on the fields in a model
* Share validation between the model and the form
* Keep it **DRY**!


Additional Django features
==========================

* Users, authentication and permissions
* Internationalization and localization
* Excellent security features
* Much much more!

