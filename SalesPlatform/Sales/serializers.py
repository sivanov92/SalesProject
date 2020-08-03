from  Sales import models
from Sales.models import Users,Contacts
from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=None)
    email = serializers.CharField(max_length=None)
    position = serializers.CharField(max_length=None)
    def create(self, validated_data):
        return Users.users.create(**validated_data)
    def update(self,instance,validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.email=validated_data.get('email',instance.email)
        instance.position=validated_data.get('position',instance.position)
        instance.save()
        return instance

class ContactSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=None)
    contact_details = serializers.CharField(max_length=None)
    contact_id = serializers.IntegerField()
    def create(self, validated_data):
        return Contacts.contacts.create(**validated_data)
    def update(self,instance,validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.contact_details=validated_data.get('contact_details',instance.contact_details)
        instance.contact_id=validated_data.get('contact_id',instance.contact_id)
        instance.save()
        return instance

