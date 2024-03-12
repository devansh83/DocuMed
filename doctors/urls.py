from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from doctors import views as doctor_views
from django.contrib.auth import views as auth_views

app_name = 'doctor'

urlpatterns = [
    path('', views.home, name='doctor-home'),
    path('prescription/', doctor_views.UploadPrescription.as_view(), name='presupload'),
    path('shared/', doctor_views.shared_documents, name='sharedoc'),  
    path('register/',doctor_views.RegisterDoc,name = 'RegisterDoc'),  
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)