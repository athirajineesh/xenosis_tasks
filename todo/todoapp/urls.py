
from django.urls import path,include
from .import views
app_name='todoapp'

urlpatterns = [

    path('',views.add,name='add'),
   # path('cbvdetails/<int:pk>/', views.Detail.as_view(), name='cbvdetails'), #pk is primarykey check notes
    path('cbvhome/', views.Tasklistview.as_view(),name='cbvhome'),
   # path('cbvupdate/<int:pk>/', views.updatetask.as_view(),name='cbvupdate'),
   # path('cbvdelete/<int:pk>/', views.deletetask.as_view(), name='cbvdelete'),
    path('update/<int:id>/', views.update, name='updatetask'),
    path('delete/<int:taskid>/', views.delete, name='deletetask'),
    path('done/<int:taskid>/', views.completed, name='completedtask'),


]

