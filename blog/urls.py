from django.urls import path
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    path('home/',views.home),
    path('about/',views.about),
    path('contact/',views.contact),
    path('dashboard/',views.dashboard),
    path('signup/',views.signup),
    path('user_login/',views.user_login),
    path('user_logout/',views.user_logout),
    
    path('update/<int:pk>/',views.update,name='update'),
    path('delete/<int:pk>/',views.delete,name='delete'),
    path('add/',views.add,name='add'),

    path('', RedirectView.as_view(url="home/")),
]
