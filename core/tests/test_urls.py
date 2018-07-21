from testarsenal import DjangoTest
import core.views as core_views
import pets.views as pet_views

class UrlTests(DjangoTest):

    def test_home_url(self):
        self.check_url_returns_view("/", core_views.home)


    def test_pet_url(self):
        self.check_url_returns_view("/pets/123/", pet_views.pet)
