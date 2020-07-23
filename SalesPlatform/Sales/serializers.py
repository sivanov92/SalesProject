from  Sales import models
from Sales.models import Users,USER_POSITION
from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    name = serializers.CharField(max_length=None)
    email = serializers.CharField(max_length=None)
    position = serializers.ChoiceField(choices=USER_POSITION,default='SalesRep')
    def create(self, validated_data):
        return Users.users.create(**validated_data)
    def update(self,instance,validated_data):
        instance.id=validated_data.get('id',instance.id)
        instance.name=validated_data.get('name',instance.name)
        instance.email=validated_data.get('email',instance.email)
        instance.position=validated_data.get('position',instance.position)
        instance.save()
        return instance

class ContactSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    name = serializers.CharField(max_length=None)
    contact_details = serializers.CharField(max_length=None)
    contact_id = serializers.IntegerField()
