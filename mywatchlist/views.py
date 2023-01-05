from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from mywatchlist.models import mywatchlist
...
# Create your views here.
def show_xml(request):
    data = mywatchlist.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = mywatchlist.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request,id):
    data = mywatchlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
def show_xml_by_id(request,id):
    data = mywatchlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

         
def show_watchlist (request):
     data_watchlist = mywatchlist.objects.all()
     context = {
         'list_watchlist': data_watchlist,
         'nama': 'Fauzil Ula Fachrudin',
         'npm' : '2106702680'

     }
     return render(request, "watchlist.html", context)
