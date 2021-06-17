from django.contrib import admin
from analytics.models import Developer, House, CustomUser
from django.utils.html import format_html
from django.urls import reverse


@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
    def site(self):
        return format_html("<a href='%s'>%s</a>" % (self.site, self.site))
    list_display = ("name", "phone_number", site)
    search_fields = ("name",)
    pass


@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ["name", "year", "status", "number_of_apartments", "availability_of_apartments", "link_to_developer"]
    search_fields = ("name",)
    list_filter = ("developer", "availability_of_apartments", "status")

    def link_to_developer(self, obj):
        link = reverse("admin:analytics_developer_change", args=[obj.developer.id])
        return format_html('<a href="%s">%s</a>' % (link, obj.developer.name))
    link_to_developer.allow_tags = True


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ["username", "first_name", "last_name", "last_login", "is_superuser"]
    search_fields = ("username", "first_name", "last_name",)
    list_filter = ("is_superuser",)
    pass


