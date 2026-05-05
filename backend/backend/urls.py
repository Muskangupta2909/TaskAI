from django.contrib import admin
from django.urls import path
from api.views import upload_doc, ask

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload-doc/', upload_doc),
    path('ask/', ask),
]