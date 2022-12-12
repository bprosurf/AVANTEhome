from django.shortcuts import render
from django.http import HttpResponse
from .models import HomeDetails


# Create your views here.


def indexPageView(request):
    return render(request, 'homepages/index.html')

def homeListingsView(request):
    data = HomeDetails.objects.all()

    context = {
        'houses' : data
    }
    return render(request, 'homepages/listings.html', context)
    
def addListingView(request):

    return render(request, 'homepages/addlisting.html')

def addListingView(request):
    if request.method == 'POST':
        house=HomeDetails()

        house.price = request.POST['price']
        house.square_ft = request.POST['square_ft']
        house.beds = request.POST['beds']
        house.baths = request.POST['baths']
        house.garage_spaces = request.POST['garage_spaces']
        house.street_address = request.POST['street_address']
        house.city = request.POST['city']
        house.state = request.POST['state']
        house.lot_size = request.POST['lot_size']
        house.year_built = request.POST['year_built']
        house.days_listed = request.POST['days_listed']

        house.save()
        return homeListingsView(request)
    else:
        return render(request, 'homepages/addlisting.html')

def deleteListingView(request):
    return render(request, 'homepages/listings.html')

def editListingView(request):
    return render(request, 'homepages/listings.html')