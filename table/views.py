from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def show_table(request):
    output = ""
    for i in range(1, 13):
        result = i * 6
        output += str(i) + " x 6 = " + str(result) + "<br>"
    return HttpResponse(output)
# Create your views here.
