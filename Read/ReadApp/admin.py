# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from ReadApp.models import AuthorModel
from ReadApp.models import NavModel
from ReadApp.models import NavItemModel
from ReadApp.models import ItemContentModel

# Register your models here.
admin.site.register(AuthorModel)
admin.site.register(NavModel)
admin.site.register(NavItemModel)
admin.site.register(ItemContentModel)