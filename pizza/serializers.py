from rest_framework.serializers import HyperlinkedModelSerializer

from pizza.models import Pizza as Pizza_Model


class PizzaSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Pizza_Model
        fields = '__all__'
