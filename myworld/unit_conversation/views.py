from django.http import HttpResponse
from django.template import loader

def index(request):
  template = loader.get_template('first_page.html')
  return HttpResponse(template.render())
