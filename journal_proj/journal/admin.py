from django.contrib import admin
from .models import Users, Trade_close, Trade

admin.site.register(Users)
admin.site.register(Trade_close)
admin.site.register(Trade)

