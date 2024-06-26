from django.contrib import admin

from .models import DanhMucSach, Sach, ThichSach, ItemSach, ThongTin
# Register your models here.
#
admin.site.register(Sach)
admin.site.register(DanhMucSach)
admin.site.register(ThichSach)
admin.site.register(ItemSach)
admin.site.register(ThongTin)
