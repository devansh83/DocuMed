from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from patients import views as patient_views
from django.contrib.auth import views as auth_views

app_name = 'patient'

urlpatterns = [
    path('', views.home, name='patient-home'),
    path('medication/', patient_views.UploadMedication.as_view(), name='medupload'),
    path('documents/', patient_views.UploadDocuments.as_view(), name='docupload'),
    path('share/', views.share_documents, name='sharedoc'),
    path('register/',patient_views.RegisterPatient,name = 'RegisterPatient'),
    path('prescription/', views.view_prescription, name='view_prescription'),
    path('scans/', views.view_scans, name='view_scans'),
    path('labreports/', views.view_lab, name='view_lab'),
    path('certificates/', views.view_certificate, name='view_certificate'),
    path('delete-medication/<int:medication_id>/', patient_views.DeleteMedication.as_view(), name='delete_medication'),  # Add this line
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
