from django.views.generic import RedirectView
from django.urls import path, include, reverse_lazy
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url=reverse_lazy("music:album_list")), name='home'),
    path('music/', include('music.urls', namespace='music')),
]
