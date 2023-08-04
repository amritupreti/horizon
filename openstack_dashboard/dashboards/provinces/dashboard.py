# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from django.utils.translation import gettext_lazy as _

import horizon
from openstack_auth import utils


class ProvinceOne(horizon.PanelGroup):
    name = _("Koshi")
    slug = "province_1"
    panels = (
        "bhojpur",
        "dhankuta",
        "illam",
        "jhapa",
        "khotang",
        "morang",
        "okhaldhunga",
        "panchthar",
        "sankhuwasabha",
        "solukhumbu",
        "sunsari",
        "taplejung",
        "terhathum",
        "udayapur",
    )


class ProvinceTwo(horizon.PanelGroup):
    name = _("Madhesh")
    slug = "province_2"
    panels = (
        "bara",
        "dhanusa",
        "mahottari",
        "parsa",
        "rautahat",
        "saptari",
        "sarlahi",
        "siraha",
    )


class ProvinceThree(horizon.PanelGroup):
    name = _("Bagmati")
    slug = "province_3"
    panels = (
        "bhaktapur",
        "chitwan", 
        "dhading",
        "dolakha",
        "kathmandu",
        "kavrepalanchok",
        "lalitpur",
        "makwanpur",
        "nuwakot",
        "ramechhap",
        "rasuwa",
        "sindhuli",
        "sindhupalchok",
    )


class ProvinceFour(horizon.PanelGroup):
    name = _("Gandaki")
    slug = "province_4"
    panels = (
        "baglung",
        "gorkha",
        "kaski",
        "lamjung",
        "manang",
        "mustang",
        "myagdi",
        "nawalparasi",
        "parbat",
        "syangja",
        "tanahu",
    )


class ProvinceFive(horizon.PanelGroup):
    name = _("Lumbini")
    slug = "province_5"
    panels = (
        "arghakhanchi",
        "banke",
        "bardiya",
        "dang",
        "eastern_rukum",
        "gulmi",
        "kapilvastu",
        "parasi",
        "palpa",
        "pyuthan",
        "rolpa",
        "rupandehi",
    )


class ProvinceSix(horizon.PanelGroup):
    name = _("Karnali")
    slug = "province_6"
    panels = (
        "dailekh",
        "dolpa",
        "humla",
        "jajarkot",
        "jumla",
        "kalikot",
        "mugu",
        "salyan",
        "surkhet",
        "western_rukum",
    )


class ProvinceSeven(horizon.PanelGroup):
    name = _("Sudurpashchim")
    slug = "province_7"
    panels = (
        "achham",
        "baitadi",
        "bajhang",
        "bajura",
        "dadeldhura",
        "darchula",
        "doti",
        "kailali",
        "kanchanpur",
    )


class Provinces(horizon.Dashboard):
    name = _("Provinces")
    slug = "provinces"
    panels = (
        ProvinceOne,
        ProvinceTwo,
        ProvinceThree,
        ProvinceFour,
        ProvinceFive,
        ProvinceSix,
        ProvinceSeven,
    )
    default_panel = "bhojpur"

    permissions = (tuple(utils.get_admin_permissions()),)


horizon.register(Provinces)
