from django.shortcuts import render

from . import models
from .models import personal_information
from django.http import HttpResponseRedirect,HttpResponse
# Create your views here.
def index(request):
    if request.method == 'GET':
        return render(request, 'BMI/index.html', context={})
    if request.method == 'POST':
        height = request.POST.get('height')
        weight = request.POST.get('weight')
        bmi =round(int(weight)/(int(height)/100)**2,1)
        # if request.META.has_key('HTTP_X_FORWARDED_FOR'):
        #     ip = request.META['HTTP_X_FORWARDED_FOR']
        # else:
        #     ip = request.META['REMOTE_ADDR']
        person = models.personal_information.objects.create(personal_weight=weight,personal_height=height,personal_bmi=bmi,)
        # person_list = personal_information.objects.filter(personal_ip=ip)
        person_list = personal_information.objects.filter(id = person.id)
        context = {
            'height':height,
            'weight':weight,
            'bmi':bmi,
            # 'ip':ip,
            'person_list':person_list
        }
        return render(request,'BMI/index.html',context)

def delete(request):
    id = request.GET.get('id')
    models.personal_information.objects.get(id=id).delete()
    return HttpResponseRedirect('/bmi/index/')