from django.contrib import admin
from django.urls import path, include

service_name = 'miniLink'

urlpatterns = [
    path(f'{service_name}/admin/', admin.site.urls),
    path('', include('shortener.urls')),
]

# Admin Site
admin.site.site_header = "MiniLink Administration"
admin.site.site_title = "MiniLink Administration"
admin.site.index_title = "Welcome to MiniLink Administration"
