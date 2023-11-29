# mi_proyecto/urls.py
from django.contrib import admin
from django.urls import include, path
from mi_app.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mi_app/', include('mi_app.urls')),
    path('', home, name='home'),
]
