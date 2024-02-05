from django.shortcuts import render

from .models import place
from .models import theme


# Create your views here.
def demo(request):
    obj = place.objects.all()
    sub = theme.objects.all()

    return render(request, "index.html", {'result': obj, 'name': sub, })

# def home(request):
#     sub = theme.objects.all()
#     return render(request, "index.html", {'name': sub})

# def addition(request):
#     x = int(request.GET['num1'])
#     y = int(request.GET['num2'])
#     res = x + y
#     return render(request, "result.html", {'result': res})
