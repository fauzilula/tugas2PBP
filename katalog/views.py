from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_katalog(request):
     data_katalog = CatalogItem.objects.all()
     context = {
         'list_barang': data_katalog,
         'nama': 'Fauzil Ula Fachrudin',
         'NPM': '2106702680'   
     }
     return render(request, "katalog.html", context)