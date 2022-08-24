from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse



def index(request):
  template = loader.get_template('first_page.html')
  return HttpResponse(template.render({},request))



def getnumber(request):
    global first_num
    first_num = request.POST['first_num']
    return HttpResponseRedirect(reverse('result'))


def result(request):
  template = loader.get_template('second_page.html')
  last = int(first_num) * 100
  context = {
    'last': last , 'first_num' : first_num
  }
  return HttpResponse(template.render(context,request))
