from django.contrib import admin
from django.urls import path
from django.urls import include
from AppAero.views import inicio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('AppAero/', include('AppAero.urls')),
]
