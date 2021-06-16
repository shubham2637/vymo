from rest_framework import serializers
from foodvymo.models import Merchant


class MerchantSerializer( serializers.ModelSerializer ):
    class Meta:
        model = Merchant
        fields = '__all__'
