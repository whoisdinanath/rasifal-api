from rest_framework import serializers
from .models import Rasifal, Rasifal_Desc


class RasifalSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()

    class Meta:
        model = Rasifal_Desc
        fields = ['title', 'description', 'date']

    def get_title(self, obj):
        return obj.rasi.title