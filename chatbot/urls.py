from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('casos/', views.CasosGuatemala),
    path('admin/', admin.site.urls),
]
