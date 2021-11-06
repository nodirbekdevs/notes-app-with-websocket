from django.contrib import admin
from django.urls import path, include
from notes.routers import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/notes/', include('notes.urls'))
    path('notes/', include(router.urls))
]
