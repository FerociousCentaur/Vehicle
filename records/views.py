from django.shortcuts import render
from .models import Record
from .forms import ImageUpload
from datetime import datetime
# Create your views here.

def homepage(request):
    if request.method=='POST':
        form = ImageUpload(request.POST, request.FILES)
        if form.is_valid():
            text_number = form.cleaned_data['number']
            if text_number:
                prev = Record.objects.filter(registration_no=text_number)
                if prev:
                    prev = prev[0]
                    prev.exit = datetime.now()
                    prev.save()
                else:
                    details = GetDetails(text_number)

                    rec = Record(owner=details['Owner Name'],brand=details['Maker Model'],chasi_number=details[''],registration_no=details,registartion_date=details,engine_no=details,vehicle_class=details,fuel=details['Fuel Type'])
                    rec.save()
            else:
                number = GetNumber(form.cleaned_data['image'])
                return render(request,'home.html',{'form':ImageUpload(initial={'number': number})})
    form = ImageUpload()
    return render(request, 'home.html',{'form':form})


def GetNumber(img):
    pass


def GetDetails(number):
    pass