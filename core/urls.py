from django.urls import path, include
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls import handler404
import core.views as core_views
import pets.views as pet_views
from django.conf import settings

urlpatterns = [
 path(r"", core_views.home),
 path(r"pets/", pet_views.pets),
 path(r"pets/<slug:id>/", pet_views.pet),
 path(r"terms/", core_views.terms),
 path(r"admin/", admin.site.urls),
 path(r"upload/", core_views.upload),
 path(r"help/", core_views.help)
] + static(
 settings.MEDIA_URL,
 document_root=settings.MEDIA_ROOT
)

handler404 = core_views.not_found
