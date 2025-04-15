from django.urls import path
from netbox.views.generic import ObjectChangeLogView

from . import models, views


urlpatterns = (
    path("prefix-statss/", views.prefixstatsListView.as_view(), name="prefixstats_list"),
    path("prefix-statss/add/", views.prefixstatsEditView.as_view(), name="prefixstats_add"),
    path("prefix-statss/<int:pk>/", views.prefixstatsView.as_view(), name="prefixstats"),
    path("prefix-statss/<int:pk>/edit/", views.prefixstatsEditView.as_view(), name="prefixstats_edit"),
    path("prefix-statss/<int:pk>/delete/", views.prefixstatsDeleteView.as_view(), name="prefixstats_delete"),
    path(
        "prefix-statss/<int:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="prefixstats_changelog",
        kwargs={"model": models.prefixstats},
    ),
)
