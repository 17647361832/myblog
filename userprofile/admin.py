from django.contrib import admin

# Register your models here.
from userprofile.models import Profile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'UserProfile'


# 将Profile关联到User中
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline, )


# 重新注册User
admin.site.unregister(User)
admin.site.register(User, UserAdmin)