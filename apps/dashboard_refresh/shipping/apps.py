import oscar.apps.dashboard.shipping.apps as apps


class ShippingDashboardConfig(apps.ShippingDashboardConfig):
    label = 'shipping_dashboard_refresh'
    name = 'apps.dashboard_refresh.shipping'
