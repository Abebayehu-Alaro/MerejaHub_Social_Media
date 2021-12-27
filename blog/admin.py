from django.contrib import admin
from blog.models import Post, Comment, Preference, Tag


admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Preference)
admin.site.register(Tag)
