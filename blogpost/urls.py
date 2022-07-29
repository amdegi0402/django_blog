#from django.contrib import admin
from django.urls import path
from .views import BlogList, BlogDetail, BlogCreate, BlogUpdate, BlogDelete
from .views import signupview, loginview, listview


urlpatterns = [
    #path('list/', BlogList.as_view(), name='list'),
    path('detail/<int:pk>/', BlogDetail.as_view(), name='detail'),
    path('create/', BlogCreate.as_view(), name='create'),
    path('delete/<int:pk>',BlogDelete.as_view(), name='delete'),
    path('update/<int:pk>', BlogUpdate.as_view(), name='update'),
    path('signup/', signupview, name='signup'),
    path('login/', loginview, name='login'),
    path('list/', listview, name='list'),
]