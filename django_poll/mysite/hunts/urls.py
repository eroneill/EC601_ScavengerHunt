from django.urls import path,include

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/',views.DetailView.as_view(),name = 'detail'),
    path('<int:pk>/results/',views.ResultView.as_view(),name='resutls'),
    path('nested_admin/', include('nested_admin.urls')),
]
 