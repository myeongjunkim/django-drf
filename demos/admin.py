from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'content', 'created_at', 'view_count', 'writer')
    list_filter = ('created_at',)
    search_fields = ('id', 'writer')
    search_help_text = '게시판 번호, 작성자 검색이 가능합니다.'

admin.site.register(Comment)
