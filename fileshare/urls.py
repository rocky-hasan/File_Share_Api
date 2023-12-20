from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from file_api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('download/<uid>/', views.download),
    path('fileupload/',views.FileUploadApi.as_view()),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
