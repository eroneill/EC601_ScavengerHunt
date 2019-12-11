from django.urls import path,include


from . import views
app_name = 'hunts'
urlpatterns = [
	path('',views.HuntView.as_view(),name='index'),
	path('<int:pk>/',views.DetailView.as_view(),name = 'detail'),
	path('<int:hunt_id>/sub/',views.sub,name='sub'),
	path('wrong/',views.Wrong.as_view(),name = 'wrong'),
	path('right/',views.Right.as_view(),name='right'),
	path('done/',views.Done.as_view(),name='done'),
	path('answered/',views.Answered.as_view(),name='answered'),
	path('nested_admin/', include('nested_admin.urls')),

]

