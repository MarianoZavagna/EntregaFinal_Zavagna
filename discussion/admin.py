from django.contrib import admin

from discussion.models import Discussion, Comment


admin.site.register(Discussion)
admin.site.register(Comment)
