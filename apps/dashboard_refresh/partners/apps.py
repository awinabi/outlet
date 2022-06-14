import oscar.apps.dashboard.partners.apps as apps


class PartnersDashboardConfig(apps.PartnersDashboardConfig):
    label = 'partners_dashboard_refresh'
    name = 'apps.dashboard_refresh.partners'
