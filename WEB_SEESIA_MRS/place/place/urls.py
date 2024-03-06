from django.contrib import admin
from django.urls import path
from place import settings
from app import views
from app.views import AppointmentView, info_view
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('appointment/', AppointmentView.as_view(), name='appointment'),
    path('info/', views.info_view, name='info'),
    path('post/', views.create_post, name='add_post'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)