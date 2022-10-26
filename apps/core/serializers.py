from rest_framework import serializers
from .models import (
    Gisement,
    Site
)


class SiteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Site
        fields = '__all__'


class GisementSerializer(serializers.ModelSerializer): 
    
    site = SiteSerializer(many=True, required=False)
    
    class Meta:
        model = Gisement
        fields = ["pk", "name", "site"]
