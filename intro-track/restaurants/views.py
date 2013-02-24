from django.shortcuts import render, redirect, get_object_or_404
from restaurants import models, forms

def home(request):
    return render(request, "home.html", {'title': "Home"})


def contact(request):
    return render(request, "contact.html", {'title': "Contact"})


def restaurant_list(request):
	context = {'title': 'Restaurant List',
			   'restaurants': models.Restaurant.objects.all()
			  }
	return render(request, "restaurant_list.html", context)

def restaurant_detail(request, pk):
	restaurant = get_object_or_404(models.Restaurant, pk=pk)
	context = {'title': 'Restaurant Detail',
	           'restaurant': restaurant,
	           'reviews': restaurant.review_set.all(),}

	return render(request, "restaurant_detail.html", context) 

def write_review(request, pk):
	restaurant = get_object_or_404(models.Restaurant, pk=pk)
	if request.method == 'GET':
		form = forms.ReviewForm()
	else:
		form = forms.ReviewForm(request.POST)
		if form.is_valid():
			review = form.save(commit=False)
			review.restaurant = restaurant
			review.save()
			return redirect('restaurant_detail', restaurant.pk)
	return render(request, "restaurant_review.html", {
		'title':'Write Review',
    	'restaurant': restaurant,
	    'form': form,
	})












