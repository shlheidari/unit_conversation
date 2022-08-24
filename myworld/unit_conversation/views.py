from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse



def index(request):
  template = loader.get_template('first_page.html')
  return HttpResponse(template.render({},request))



def getnumber(request):
    global first_num, first_unit
    first_num = request.POST['first_num']
    first_unit = request.POST['first_unit']
    return HttpResponseRedirect(reverse('result'))


def result(request):
  template = loader.get_template('second_page.html')
  if first_unit == 'Km' : last = int(first_num) * 1000
  elif first_unit == 'm' : last = int(first_num) * 1
  elif first_unit == 'cm' : last = int(first_num) / 100
  elif first_unit == 'mm' : last = int(first_num) / 1000

  context = {
    'last': last , 'first_num' : first_num , 'first_unit' : first_unit
  }
  return HttpResponse(template.render(context,request))
