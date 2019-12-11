from django.urls import path
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
	path('signup/',views.SignUp.as_view(), name = 'signup'), path('login/', views.login_request, name='login'), path('', TemplateView.as_view(template_name='home.html'), name='home'),
]