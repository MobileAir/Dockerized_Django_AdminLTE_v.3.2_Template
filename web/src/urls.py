from django.conf import settings
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
from django.conf.urls.static import static
from app.sitemaps import StaticViewSitemap, ProfileSitemap
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


sitemaps: dict = {
    'static': StaticViewSitemap,
    'profile': ProfileSitemap,
}

urlpatterns = [
    path('', include('app.urls')),
    path('admin/', admin.site.urls),
    path('admin/defender/', include('defender.urls')),
    path('adminlte/', include('adminlte.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    path('accounts/', include('allauth.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

handler404 = 'app.views.custom_handler404'
handler500 = 'app.views.custom_handler500'


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
