from django.urls import path, include




from . import views
app_name = "jitter"
urlpatterns = [
# path('admin/', views.index, name='admin'),
    path('', views.index, name='index'),
 path('mainbunk/', views.mainbunk, name='mainbunk'),
path('mainuser/', views.mainuser, name='mainuser'),
path('mainuser/<int:pk>/', views.view_bunks, name='userbunks'),
path('bunkform/', views.bunkform, name='bunkform'),
path('formfailed/', views.formfailed, name='formfailed'),

]
