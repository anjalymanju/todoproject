from . import views
from django.urls import path

urlpatterns = [

    path('',views.demo,name='demo'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('list/',views.Listview.as_view(),name='list'),
    path('detail/<int:pk>/', views.Detailview.as_view(), name='detail'),
    path('cvbupdate/<int:pk>/', views.Updateview.as_view(), name='cvbupdate'),
    path('delete/<int:pk>/', views.Deleteview.as_view(), name='delete'),


]
