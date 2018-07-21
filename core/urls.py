from django.urls import path, include
import pets.views as pet_views

urlpatterns = [
 path(r"pet/<slug:id>/", pet_views.pet),
]
