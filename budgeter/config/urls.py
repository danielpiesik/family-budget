from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),

    path('budgets/', include('budgets.urls')),
    path('users/', include('users.urls')),
]
