from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

def index(request):
  template = loader.get_template('first_page.html')
  return HttpResponse(template.render({},request))

def result(request):
  template = loader.get_template('second_page.html')
  return HttpResponse(template.render({},request))

def getnumber(request):
    x = request.POST['first']
    return HttpResponseRedirect(reverse('result'))
