from django.urls import path
from . import views
urlpatterns = [
    path('add/', views.musician_list, name='musician'),
    path('edit_musiciian/<int:id>', views.edit_musician, name='edit_musician'),
]
