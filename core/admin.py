from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
     list_display = ["id", "nomi", "daromadi"]
     list_display_links = ["id", "nomi"]
     
     def get_list_display(self, request):
          if request.user.is_authenticated and request.user.username.startswith("m"):
               return ["id"]
          return self.list_display

admin.site.register(Post, PostAdmin)