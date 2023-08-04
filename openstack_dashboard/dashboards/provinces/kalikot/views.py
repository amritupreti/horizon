
from horizon import tabs

from openstack_dashboard.dashboards.provinces.district import tabs as district_tabs


class IndexView(tabs.TabbedTableView):
    tab_group_class = district_tabs.DistrictTabs
    template_name = 'district.html'
    page_title = "Kalikot"

    def get_data(self, request, context, *args, **kwargs):
        # Add data to the context here...
        return context
