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
    path('login/', auth_views.LoginView.as_view(template_name='patients/Login.html'),name = 'patlogin')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

