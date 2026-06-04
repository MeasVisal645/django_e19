from django.contrib import admin
from django.urls import path, include
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('category/', include('category.urls')),
    path('welcome/', views.welcome_view, name='welcome'),
]
