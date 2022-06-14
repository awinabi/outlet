import oscar.apps.dashboard.reviews.apps as apps


class ReviewsDashboardConfig(apps.ReviewsDashboardConfig):
    label = 'reviews_dashboard_refresh'
    name = 'apps.dashboard_refresh.reviews'
