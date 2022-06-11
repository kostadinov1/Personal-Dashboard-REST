from django.contrib.auth import get_user_model
from rest_framework import serializers

UserModel = get_user_model()


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = (UserModel.USERNAME_FIELD, 'password')

    def create(self, validated_data):
        # hide plain text password in db
        user = super(CreateUserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    # called on return
    def to_representation(self, instance):
        result = super(CreateUserSerializer, self).to_representation(instance)
        # get the instance and pop its password
        result.pop('password')
        return result

    def validate(self, date):
        # invoke password validators
        return super(CreateUserSerializer, self).validate(date)
