from .views import index
from django.contrib import admin
from django.urls import path

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', index, name='index')
]
