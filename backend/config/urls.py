"""
URL configuration for config project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

def home(request):
    return JsonResponse({"status": "Backend is running 🚀"})

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('api/auth/', include('apps.accounts.urls')),
    path('api/scores/', include('apps.scores.urls')),
    path('api/charities/', include('apps.charities.urls')),
    path('api/subscriptions/', include('apps.subscriptions.urls')),
    path('api/draws/', include('apps.draws.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
