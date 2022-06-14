import oscar.apps.dashboard.ranges.apps as apps


class RangesDashboardConfig(apps.RangesDashboardConfig):
    label = 'ranges_dashboard_refresh'
    name = 'apps.dashboard_refresh.ranges'
