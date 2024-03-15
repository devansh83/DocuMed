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
    path('<str:doctor_id>/profile/',doctor_views.profile,name='profile'),
    # path('shared-documents/', views.shared_documents, name='shared_documents'),
    path('<str:patient_name>/documents/', views.patient_documents, name='patient_documents'),  
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)