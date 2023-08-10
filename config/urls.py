# from django.contrib import admin
# from django.urls import path
# from texnoshop import views

# urlpatterns=[
# 	    path('admin/', admin.site.urls),
#         path('',views.home,name="home"),
#         ]


from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('texnoshop.urls')),
    path('auth/', include('authentication.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)