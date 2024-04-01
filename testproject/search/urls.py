from . import views
from django.urls import path


urlpatterns = [
    path('',views.ListNewsView.as_view()),
    path('index',views.ListindexView.as_view(),name='index'),
    path('delete/<int:pk>',views.deletecomment,name='delete'),
    path('company',views.ListcompanyView.as_view(),name='company'),
    path('faq',views.ListfaqView.as_view(),name='faq'),
    path('contact',views.ListcontactView.as_view(),name='contact'),
    path('service',views.ListserviceView.as_view(),name='service'),
    path('service2',views.Listservice2View.as_view(),name='service'),
    path('comments', views.create_comment, name="create_comment"),
    path('logout/',views.logout_view,name='logout'),

] 