import subprocess

province_1_districts = {
    "Bhojpur",
    "Dhankuta",
    "Ilam",
    "Jhapa",
    "Khotang",
    "Morang",
    "Okhaldhunga",
    "Panchthar",
    "Sankhuwasabha",
    "Solukhumbu",
    "Sunsari",
    "Taplejung",
    "Terhathum",
    "Udayapur",
}

province_2_districts = {
    "Bara",
    "Dhanusha",
    "Mahottari",
    "Parsa",
    "Rautahat",
    "Saptari",
    "Sarlahi",
    "Siraha",
}

province_3_districts = {
    "Bhaktapur",
    "Chitwan",
    "Dhading",
    "Dolakha",
    "Kathmandu",
    "Kavrepalanchok",
    "Lalitpur",
    "Makwanpur",
    "Nuwakot",
    "Ramechhap",
    "Rasuwa",
    "Sindhuli",
    "Sindhupalchok",
}

province_4_districts = {
    "Baglung",
    "Gorkha",
    "Kaski",
    "Lamjung",
    "Manang",
    "Mustang",
    "Myagdi",
    "Nawalpur",
    "Parbat",
    "Syangja",
    "Tanahun",
}

province_5_districts = {
    "Arghakhanchi",
    "Banke",
    "Bardiya",
    "Dang",
    "Eastern_Rukum",
    "Gulmi",
    "Kapilvastu",
    "Parasi",
    "Palpa",
    "Pyuthan",
    "Rolpa",
    "Rupandehi",
}

province_6_districts = {
    "Dailekh",
    "Dolpa",
    "Humla",
    "Jajarkot",
    "Jumla",
    "Kalikot",
    "Mugu",
    "Salyan",
    "Surkhet",
    "Western_Rukum",
}

province_7_districts = {
    "Achham",
    "Baitadi",
    "Bajhang",
    "Bajura",
    "Dadeldhura",
    "Darchula",
    "Doti",
    "Kailali",
    "Kanchanpur",
}

nepal_districts = (
    province_1_districts.union(province_2_districts)
    .union(province_3_districts)
    .union(province_4_districts)
    .union(province_5_districts)
    .union(province_6_districts)
    .union(province_7_districts)
)


# tables_py_content = '''
# from django.utils.translation import gettext_lazy as _

# from horizon import tables


# class MyFilterAction(tables.FilterAction):
#     name = "myfilter"


# class InstancesTable(tables.DataTable):
#     name = tables.Column('name', \
#                             verbose_name=_("Name"))
#     status = tables.Column('status', \
#                             verbose_name=_("Status"))
#     zone = tables.Column('availability_zone', \
#                             verbose_name=_("Availability Zone"))
#     image_name = tables.Column('image_name', \
#                                 verbose_name=_("Image Name"))

#     class Meta(object):
#         name = "instances"
#         verbose_name = _("Instances")
#         table_actions = (MyFilterAction,)
# '''


# tabs_py_content = '''
# from django.utils.translation import gettext_lazy as _

# from horizon import exceptions
# from horizon import tabs

# from openstack_dashboard import api
# from openstack_dashboard.dashboards.provinces.mypanel import tables


# class InstanceTab(tabs.TableTab):
#     name = _("Instances Tab")
#     slug = "instances_tab"
#     table_classes = (tables.InstancesTable,)
#     template_name = ("horizon/common/_detail_table.html")
#     preload = False

#     def has_more_data(self, table):
#         return self._has_more

#     def get_instances_data(self):
#         try:
#             marker = self.request.GET.get(
#                         tables.InstancesTable._meta.pagination_param, None)

#             instances, self._has_more = api.nova.server_list(
#                 self.request,
#                 search_opts={'marker': marker, 'paginate': True})

#             return instances
#         except Exception:
#             self._has_more = False
#             error_message = _('Unable to get instances')
#             exceptions.handle(self.request, error_message)

#             return []

# class DistrictTabs(tabs.TabGroup):
#     slug = "mypanel_tabs"
#     tabs = (InstanceTab,)
#     sticky = True
# '''


view_py_content = '''
from horizon import tabs

from openstack_dashboard.dashboards.provinces.district import tabs as district_tabs


class IndexView(tabs.TabbedTableView):
    tab_group_class = district_tabs.DistrictTabs
    template_name = 'district.html'
    page_title = "page_title_replace"

    def get_data(self, request, context, *args, **kwargs):
        # Add data to the context here...
        return context
'''


# for district in nepal_districts:
#     with open(f"openstack_dashboard/dashboards/provinces/{district.lower()}/templates/{district.lower()}/index.html", "w") as f:
#         index_html = '''
#             {% extends 'base.html' %}
#             {% load i18n %}
#             {% block title %}{% trans "my_panel" %}{% endblock %}

#             {% block page_header %}
#                 {% include "horizon/common/_page_header.html" with title=_("my_panel") %}
#             {% endblock page_header %}

#             {% block main %}
#                 <div class="row">
#                     <div class="col-sm-12">
#                         {{ tab_group.render }}
#                     </div>
#                 </div>
#             {% endblock %}
#         '''.replace("my_panel", district)
#         f.write(index_html)
        
# for district in nepal_districts:
#     with open(f"openstack_dashboard/dashboards/provinces/{district.lower()}/tabs.py", "w") as f:
#         tabs_py = tabs_py_content.replace("mypanel", district.lower())
#         f.write(tabs_py)

# for district in nepal_districts:
#     with open(f"openstack_dashboard/dashboards/provinces/{district.lower()}/tables.py", "w") as f:
#         f.write(tables_py_content)

# for district in nepal_districts:
#     with open(f"openstack_dashboard/dashboards/provinces/{district.lower()}/views.py", "w") as f:
#         view_py = view_py_content.replace("mypanel", district.lower())
#         f.write(view_py)


for district in nepal_districts:
    with open(f"openstack_dashboard/dashboards/provinces/{district.lower()}/views.py", "w") as f:
        district_name = district.replace("_", " ")
        view_py = view_py_content.replace("page_title_replace", district_name)
        f.write(view_py)
