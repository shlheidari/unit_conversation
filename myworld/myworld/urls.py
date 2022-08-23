from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('unit_conversation/', include('unit_conversation.urls')),
    path('admin/', admin.site.urls),
]
