import oscar.apps.dashboard.vouchers.apps as apps


class VouchersDashboardConfig(apps.VouchersDashboardConfig):
    label = 'vouchers_dashboard_refresh'
    name = 'apps.dashboard_refresh.vouchers'
