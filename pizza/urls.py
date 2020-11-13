from rest_framework.routers import DefaultRouter

from pizza.views import PizzaViewSet

router = DefaultRouter()

router.register('pizza', PizzaViewSet)


urlpatterns = router.urls
