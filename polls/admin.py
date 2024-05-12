from django.contrib import admin
from .models import User, Events, Message, Profile, Template

admin.site.register(User)
admin.site.register(Events)
admin.site.register(Message)
admin.site.register(Profile)
admin.site.register(Template)