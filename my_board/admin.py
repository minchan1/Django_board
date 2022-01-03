from django.contrib import admin
from .models import board

# Register your models here.
class boardAdmin( admin.ModelAdmin ):
    # 관리자 페이지에서 화면에 보여지는 목록
    list_display = ('createDate', 'user', 'subject' )

    # 링크 새로 정의 (제목을 클릭해서 상세페이지 이동)
    nlist_display_liks = ['subject']

admin.site.register(board, boardAdmin)
