from django.urls import path
from netbox.views.generic import ObjectChangeLogView

from . import models, views


urlpatterns = (
    path("tests/", views.testListView.as_view(), name="test_list"),
    path("tests/add/", views.testEditView.as_view(), name="test_add"),
    path("tests/<int:pk>/", views.testView.as_view(), name="test"),
    path("tests/<int:pk>/edit/", views.testEditView.as_view(), name="test_edit"),
    path("tests/<int:pk>/delete/", views.testDeleteView.as_view(), name="test_delete"),
    path(
        "tests/<int:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="test_changelog",
        kwargs={"model": models.test},
    ),
)
