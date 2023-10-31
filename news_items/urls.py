from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:source_id>/", views.source_list),
    path("<int:source_id>/<int:question_id>", views.detail),
]
