import oscar.apps.dashboard.offers.apps as apps


class OffersDashboardConfig(apps.OffersDashboardConfig):
    label = 'offers_dashboard_refresh'
    name = 'apps.dashboard_refresh.offers'
