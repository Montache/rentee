from django.shortcuts import render
from django import forms
from.models import Listing, RenteeUser, Category
from .forms import ListingForm
from django.http import HttpResponseRedirect

# Create your views here.

def Homepage(request):
    listings = Listing.objects.all()
    categorys = Category.objects.all()
    return render(request, 'Home/Home.html',{
        'listings': listings,
        'categorys':categorys,
    })

def ViewListing(request, listing_id):
    listing = Listing.objects.get(pk=listing_id)
    return render (request, 'Home/ViewListing.html', {
        'listing':listing,
    })

def AddListing(request):
    submitted = False
    if request.method=='POST':
        form=ListingForm(request.POST, request.FILES)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.Owner=request.user.id
            # listing.Owner=request.user
            listing.save()
            return HttpResponseRedirect('/AddListing?submitted=True')
    else:
        form=ListingForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request, 'Home/AddListing.html',{
        'submitted':submitted,
        'form':form
    })

# def ViewCategories(request, Category_id):
#     category = Category.objects.get(pk=category_id)
#     return render (request, 'Home/ViewListing.html', {
#         'category':category
#     })

# def VisitCategory(request):
#     viewcategory = Category.objects.all()
#     return render(request, 'Home/Home.html',{
#         'viewcategory': viewcategory
        
#     })












