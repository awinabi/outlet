from oscar.apps.dashboard.catalogue import views as oscar_catalogue_dashboard_views


class ProductListView(oscar_catalogue_dashboard_views.ProductListView):

    template_name = 'oscar/dashboard_refresh/catalogue/product_list.html'
