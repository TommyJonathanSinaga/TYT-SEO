from bert.views import BertViewSet
from django.contrib import admin
from django.urls import include, path
from extractor.views import ExtractorViewSet, SitemapViewSet
from internalLinks.views import InternalLinksViewSet
from keywords.views import YakeViewSet
from lighthouse.views import LighthouseResultViewSet, LighthouseViewSet
from security.views import SecurityResultViewSet, SecurityViewSet
from org.views import WebsiteViewSet
from organizations.backends import invitation_backend
from rest_framework import routers
from users.views import GroupViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'api/extractor', ExtractorViewSet, basename='Extractor')
router.register(r'api/sitemap', SitemapViewSet, basename='Sitemap')
router.register(r'api/lighthouse_details', LighthouseResultViewSet, basename='Ligthouse_Results')
router.register(r'api/lighthouse', LighthouseViewSet, basename='Ligthouse')
router.register(r'api/security_details', SecurityResultViewSet, basename='Security_Results')
router.register(r'api/security', SecurityViewSet, basename='Security')
router.register(r'api/internal_links', InternalLinksViewSet)
router.register(r'api/summarize', BertViewSet, basename='Bert')
router.register(r'api/keywords/yake', YakeViewSet, basename='Yake')
router.register(r'api/website_user', WebsiteViewSet, basename='Website')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('organizations.urls')),
    path('invitations/', include(invitation_backend().get_urls()))
]
