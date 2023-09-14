from datetime import date

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Review


# Create your views here.

def reviews(request):
    reviews = Review.objects.all()
    return render(request, 'review/reviews.html', {'reviews': reviews})


@login_required()
def add_review(request):
    if request.method == "POST":
        item = Review()
        item.title = request.POST.get("title")
        item.review_text = request.POST.get("review_text")
        item.stars = request.POST.get("stars")
        item.username = request.user.get_username()
        item.date_of_review = date.today()
        item.save()
        return redirect('/reviews/')

    else:
        return render(request, 'review/add_review.html')
