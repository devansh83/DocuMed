from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from patients import views as patient_views

urlpatterns = [
    path('', views.home, name='patient-home'),
    path('medication/', patient_views.UploadMedication.as_view(), name='medupload'),
    path('documents/', patient_views.UploadDocuments.as_view(), name='docupload'),
    path('share/', views.share_documents, name='sharedoc'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

