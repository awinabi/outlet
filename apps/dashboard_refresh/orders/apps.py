import oscar.apps.dashboard.orders.apps as apps


class OrdersDashboardConfig(apps.OrdersDashboardConfig):
    label = 'orders_dashboard_refresh'
    name = 'apps.dashboard_refresh.orders'
