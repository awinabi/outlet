from django.apps import apps
from django.urls import path, include

import oscar.apps.dashboard.apps as oscar_apps
from oscar.core.loading import get_class


class DashboardRefreshConfig(oscar_apps.DashboardConfig):
    label = 'dashboard_refresh'
    name = 'apps.dashboard_refresh'

    def ready(self):
        self.index_view = get_class('dashboard_refresh.views', 'IndexView')
        self.catalogue_app = apps.get_app_config('catalogue_dashboard_refresh')

    def get_urls(self):
        from django.contrib.auth import views as auth_views

        urls = ([
            path('', self.index_view.as_view(), name='index'),
            path('catalogue/', include(self.catalogue_app.urls[0])),
        ], "dashboard_refresh")

        return urls
