
from django.contrib import admin
from django.urls import path, include #include アプリのurls.pyを呼び出すために必要なもの
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blogpost.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
staic(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
