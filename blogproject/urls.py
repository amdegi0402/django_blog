
from django.contrib import admin
from django.urls import path, include #include アプリのurls.pyを呼び出すために必要なもの

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blogpost.urls')),
]
