from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from pizza.models import Pizza as Pizza_Model
from pizza.serializers import PizzaSerializer


class PizzaViewSet(ModelViewSet):
    queryset = Pizza_Model.objects.all()
    serializer_class = PizzaSerializer
    permission_classes = [AllowAny]
