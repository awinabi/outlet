import oscar.apps.dashboard.users.apps as apps


class UsersDashboardConfig(apps.UsersDashboardConfig):
    label = 'users_dashboard_refresh'
    name = 'apps.dashboard_refresh.users'
