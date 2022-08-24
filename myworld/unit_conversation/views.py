from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse



def index(request):
  template = loader.get_template('first_page.html')
  return HttpResponse(template.render({},request))



def getnumber(request):
    global first_num, first_unit, last_unit
    first_num = request.POST['first_num']
    first_unit = request.POST['first_unit']
    last_unit = request.POST['last_unit']
    return HttpResponseRedirect(reverse('result'))


def result(request):
  template = loader.get_template('second_page.html')
  if first_unit == 'Km' : middle = int(first_num) * 1000
  elif first_unit == 'm' : middle = int(first_num)
  elif first_unit == 'cm' : middle = int(first_num) / 100
  elif first_unit == 'mm' : middle = int(first_num) / 1000

  if last_unit == 'Km' : last = middle / 1000
  elif last_unit == 'm' : last = middle
  elif last_unit == 'cm' : last = middle * 100
  elif last_unit == 'mm' : last = middle * 1000

  context = {
    'last': last , 'first_num' : first_num , 'first_unit' : first_unit , 'last_unit' : last_unit
  }
  return HttpResponse(template.render(context,request))
