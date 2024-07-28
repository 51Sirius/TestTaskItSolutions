from parsing.models import Advert
from rest_framework import serializers


class AdvertSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Advert
        fields = ['title', 'reference_id', 'author', 'views_count', 'position']