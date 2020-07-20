from  Sales import models
from models import Users,USER_POSITION
from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    name = serializers.CharField(max_length = 200)
    email = serializers.CharField(max_length = 200)
    position = serializers.ChoiceField(choices=USER_POSITION,defailt='SalesRep')
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
    id=serializers.IntegerField(max_length = 10)
    name = serializers.CharField(max_length = 200)
    contact_details = serializers.CharField(max_length = 300)
    contact_id = serializers.IntegerField(max_length=10)
