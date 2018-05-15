from django.urls import path
from . import views
app_name='rel_app'
urlpatterns = [
    path('',views.index,name='index'),
    path('relative/',views.relative,name='relative'),
    path('others/',views.others,name='others'),
]
