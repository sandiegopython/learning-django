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

    class ReviewForm(forms.Form):
        title = forms.CharField()
        body = forms.CharField()

.. Regex validators, number within set of values, etc.
.. Date widgets, mutliple select widgets, etc.

* Custom validators
* Custom widgets
* Groups of forms


Using forms with class-based views
==================================

.. Discuss GET vs. POST requests
.. Mention form verification and show empty form submission

.. code-block:: python

   class CreateReviewView(TemplateView):
       template_name = 'create_review.html'
   
       def get(self, request, pk):
           self.restaurant = get_object_or_404(Restaurant, pk=pk)
           self.form = ReviewForm()
           return super(CreateReviewView, self).get(request, pk)
   
       def post(self, request, pk):
           self.restaurant = get_object_or_404(Restaurant, pk=pk)
           self.form = ReviewForm(request.POST)
           if self.form.is_valid():
               review = self.form.save(commit=False)
               review.restaurant = self.restaurant
               review.save()
               return redirect(self.restaurant)
           return self.render_to_response(self.get_context_data(request, pk)) 


Displaying forms with templates
===============================

.. Don't go into detail on CSRF other than it is a Django security feature

.. code-block:: html

    <form action="{% url restaurants.views.add_review %}" method="post">
      {% csrf_token %}
      {{ form.as_p }}
      <input type="submit" value="Write Review" />
    </form>


There's a shortcut! Model forms
===============================

.. code-block:: python

    from django import forms
    from .models import Review

    class ReviewForm(forms.ModelForm):
        class Meta:
            model = Review


Model form advantages
=====================

* Create a form based on the fields in a model
* Share validation between the model and the form
* Keep it **DRY**!


Debugging forms
===============

.. code-block:: python

    % python manage.py shell
    >>> from restuarants.forms import ReviewForm
    >>> from restaurants.models import Restaurant
    >>> restaurant = Restaurant.objects.get(pk=1)
    >>> form = ReviewForm({
    ...     'title': 'Yum',
    ...     'body': 'Burgers are great!'}, instance=restaurant)
    >>> form.is_valid()
    True
    >>> form.save()
    
