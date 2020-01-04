from django.urls import path

from .views import AlbumListView, AlbumCreateView, AlbumUpdateView

app_name = 'music'

urlpatterns = [
    path('album/', view=AlbumListView.as_view(), name='album_list'),
    path('album/create/', view=AlbumCreateView.as_view(), name='album_create', ),
    path('album/<int:pk>/update/', view=AlbumUpdateView.as_view(), name='album_update'),
]
