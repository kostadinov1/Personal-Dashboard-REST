from rest_framework import serializers

from web.periodization.models import TimeCycle


class ListAllTimeCyclesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeCycle
        fields = '__all__'


class CreateTimeCycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeCycle
        fields = '__all__'


class EditTimeCycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeCycle
        fields = '__all__'


class DeleteTimeCycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeCycle
        fields = '__all__'
