from django.contrib import admin

# Register your models here.
import nested_admin
from .models import Hunt, Stop, Answer, Response, Usrs
class AnswerInline(nested_admin.NestedTabularInline):
	model = Answer
	extra = 2
	max_num = 4

class StopInline(nested_admin.NestedTabularInline):
	model = Stop
	inlines = [AnswerInline,]
	extra = 3
class HuntAdmin(nested_admin.NestedModelAdmin):
	inlines = [StopInline,]

class ResponseInline(admin.TabularInline):
	model = Response
class UsrsAdmin(admin.ModelAdmin):
	inlines = [ResponseInline,]
	
admin.site.register(Hunt, HuntAdmin)
admin.site.register(Usrs, UsrsAdmin)
admin.site.register(Response)