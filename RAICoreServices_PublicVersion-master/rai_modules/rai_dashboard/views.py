import re
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, "rai_dashboard/hello_there.html")