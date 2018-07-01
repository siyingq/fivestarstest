from django.shortcuts import render
from .models import Category, SittingDate, ParliamentRecord
from django.views import generic 

# Create your views here.
def index(request): #home page of website
    #wishful thinking: drop down select bar for all the categories available
    num_records = ParliamentRecord.objects.all().count()
    num_categories = Category.objects.all().count()
    all_categories = ParliamentRecord.objects.all()

    return render(
        request, 
        "index.html", 
        context={'num_records':num_records, 'num_categories':num_categories},
        )

class ParliamentRecordListView(generic.ListView):
    model = ParliamentRecord

    def get_queryset(self):
        pass