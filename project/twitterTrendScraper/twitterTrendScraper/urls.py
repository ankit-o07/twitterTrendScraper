
from django.contrib import admin
from django.urls import path
# from views import trending_hashtags_view
from . import views

urlpatterns = [
    path('',views.home),
    path('admin/', admin.site.urls),
    path('trending/', views.trending_hashtags_view, name='trending_hashtags'),
]
