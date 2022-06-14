from django.urls import path


import oscar.apps.dashboard.catalogue.apps as apps
from oscar.core.loading import get_class


class CatalogueDashboardConfig(apps.CatalogueDashboardConfig):
    label = 'catalogue_dashboard_refresh'
    name = 'apps.dashboard_refresh.catalogue'


    def ready(self):
        self.product_list_view = get_class('dashboard_refresh.catalogue.views',
                                           'ProductListView')

    def get_urls(self):
        urls = ([
            path('', self.product_list_view.as_view(), name='catalogue-product-list'),
        ], "dashboard_refresh")
        return urls
