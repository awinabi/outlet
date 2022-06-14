import oscar.apps.dashboard.communications.apps as apps


class CommunicationsDashboardConfig(apps.CommunicationsDashboardConfig):
    label = 'communications_dashboard_refresh'
    name = 'apps.dashboard_refresh.communications'
