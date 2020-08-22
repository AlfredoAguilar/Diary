"""
Base URL Configuration
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns

# from rest_framework import routers

# Admin Attributes
if hasattr(settings, 'ADMIN_SITE_HEADER'):
    admin.site.site_header = settings.ADMIN_SITE_HEADER
if hasattr(settings, 'ADMIN_SITE_TITLE'):
    admin.site.site_title = settings.ADMIN_SITE_TITLE
if hasattr(settings, 'ADMIN_SITE_INDEX_TITLE'):
    admin.site.index_title = settings.ADMIN_SITE_INDEX_TITLE
if hasattr(settings, 'SITE_URL'):
    admin.site.site_url = settings.SITE_URL


urlpatterns = [
    # Admin
    path('project-adm/', admin.site.urls)
]

urlpatterns += i18n_patterns(
    path('theme/', include('BaseProject.apps.admin_theme.urls')),

    # Auth
    path('', include('allauth.urls')),

    # API POSTS
    path('auth-api/', include('rest_framework.urls', namespace='rest_framework')),

    prefix_default_language=False
)

if settings.DEBUG:
    from django.conf.urls.static import static
    import debug_toolbar
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
