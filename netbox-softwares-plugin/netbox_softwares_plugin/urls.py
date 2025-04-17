from django.urls import path
from netbox.views.generic import ObjectChangeLogView

from . import models, views


urlpatterns = (
    path("softwaress/", views.SoftwaresListView.as_view(), name="softwares_list"),
    path("softwaress/add/", views.SoftwaresEditView.as_view(), name="softwares_add"),
    path("softwaress/<int:pk>/", views.SoftwaresView.as_view(), name="softwares"),
    path("softwaress/<int:pk>/edit/", views.SoftwaresEditView.as_view(), name="softwares_edit"),
    path("softwaress/<int:pk>/delete/", views.SoftwaresDeleteView.as_view(), name="softwares_delete"),
    path(
        "softwaress/<int:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="softwares_changelog",
        kwargs={"model": models.Softwares},
    ),
)
