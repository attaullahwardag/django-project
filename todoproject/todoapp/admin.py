from django.contrib import admin
from .models import Todoitem
from .models import Articles
# Register your models here.
admin.site.register(Todoitem)
admin.site.register(Articles)