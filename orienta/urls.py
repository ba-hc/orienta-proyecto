from django.urls import path, re_path
from django.contrib.staticfiles.views import serve
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("acceso/", views.account, name="account"),
    path("intereses/", views.interests, name="interests"),
    path("prioridades/", views.priorities, name="priorities"),
    path("catalogo/", views.catalog, name="catalog"),
    path("catalogo/<int:offer_id>/", views.detail, name="detail"),
    path("catalogo/<int:offer_id>/guardar/", views.save_offer, name="save_offer"),
    path("catalogo/<int:offer_id>/retirar/", views.remove_offer, name="remove_offer"),
    path("guardados/", views.saved, name="saved"),
    path("comparar/", views.comparison, name="comparison"),
    path("proceso/<uuid:process_id>/", views.process_snapshot, name="snapshot"),
    path("proceso/<uuid:process_id>/eliminar/", views.delete_process, name="delete"),
    path("salir/", views.end_session, name="logout"),
    path("health/", views.health, name="health"),
]
# Solo servidor académico loopback; en operación se usa un servidor estático.
urlpatterns += [re_path(r"^static/(?P<path>.*)$", serve, {"insecure": True})]
