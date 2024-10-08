from django.shortcuts import render


# Create your views here.
def index(request):
    cars = [
        {
            "made": "Toyota",
            "model": "Corolla",
            "year": 2015,
            "color": "red",
            "price": 5000
        },
        {
            "made": "Kia",
            "model": "Rio",
            "year": 2016,
            "color": "blue",
            "price": 6000
        }
    ]

    context = {
        "cars": cars
    }
    return render(request, 'index.html', context)
