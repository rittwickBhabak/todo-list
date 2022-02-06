from django.urls import path
from . import views 

app_name=  'myapp'

urlpatterns = [
    path("", views.home, name='home'),
    path("mark-done/<int:pk>", views.mark_done, name="mark-done"),
    # path("mark-undone/<int:pk>", views.mark_undone, name="mark-undone"),
    # path("mark-active/<int:pk>", views.mark_active, name="mark-active"),
    # path("mark-inactive/<int:pk>", views.mark_inactive, name="mark-inactive"),
]

