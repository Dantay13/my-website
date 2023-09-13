from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from personal import views

urlpatterns = [
    path('', views.resume_view, name='resume'),  # Use 'resume_view' or the appropriate view name
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('personal/', include('personal.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns


