import django.conf.urls
from django.contrib import admin
from apiwithparaapp import views
urlpatterns = [
    django.conf.urls.url(r'^admin/', admin.site.urls),
    django.conf.urls.url(r'^bubblesort/?', views.get)
]
