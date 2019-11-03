from django.urls import path,include


from . import views
app_name = 'hunts'
urlpatterns = [
	path('',views.HuntView.as_view(),name='index'),
	path('<int:pk>/',views.DetailView.as_view(),name = 'detail'),
	path('<int:hunt_id>/sub/',views.sub,name='sub'),
	path('nested_admin/', include('nested_admin.urls')),
]

