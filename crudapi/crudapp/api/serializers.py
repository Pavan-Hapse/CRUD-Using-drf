from rest_framework import serializers
from crudapp.models import Animal_info


class Animal_infoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal_info
        fields = "__all__"