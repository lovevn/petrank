from django.urls import path, include
import core.views as core_views
import pets.views as pet_views

urlpatterns = [
 path(r"", core_views.root),
 path(r"pet/<slug:id>/", pet_views.pet),
]
