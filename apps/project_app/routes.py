from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^dashboard$',views.dashboard),
    url(r'^login$',views.login),
    url(r'^register$',views.register),
    url(r'^checkout$',views.checkout),
    url(r'^reports$',views.reports),
    url(r'^products$',views.products),
    url(r'^employee_list$',views.employee_list),
    


]