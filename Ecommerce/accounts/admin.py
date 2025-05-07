from django.contrib import admin
from .models import User,Role,RolePermission,Permission

admin.site.register(User)
admin.site.register(Role)
admin.site.register(RolePermission)
admin.site.register(Permission)
