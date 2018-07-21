from django.urls import path, include
import core.views as core_views
import pets.views as pet_views

urlpatterns = [
 path(r"", core_views.home),
 path(r"pets/<slug:id>/", pet_views.pet),
]
