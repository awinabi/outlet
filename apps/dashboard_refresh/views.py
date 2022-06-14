from django.views.generic import TemplateView
from oscar.apps.dashboard import views as oscar_dashboard_views


class IndexView(oscar_dashboard_views.IndexView):

    def get_template_names(self):
        if self.request.user.is_staff:
            return ['oscar/dashboard_refresh/index.html', ]
        else:
            return ['oscar/dashboard_refresh/index_nonstaff.html', 'oscar/dashboard_refresh/index.html']
