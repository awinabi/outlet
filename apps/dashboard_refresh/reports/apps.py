import oscar.apps.dashboard.reports.apps as apps


class ReportsDashboardConfig(apps.ReportsDashboardConfig):
    label = 'reports_dashboard_refresh'
    name = 'apps.dashboard_refresh.reports'
