from rest_framework import serializers

from web.periodization.models import MacroCycle, MesoCycle, MicroCycle


class ListAllMacroCyclesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MacroCycle
        fields = '__all__'


class CreateMacroCycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MacroCycle
        fields = '__all__'


class EditMacroCycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MacroCycle
        fields = '__all__'


class DeleteMacroCycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MacroCycle
        fields = '__all__'


# =================  Meso Cycle Serializers ====================== #

class ListAllMesoCyclesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MesoCycle
        fields = '__all__'


class CreateMesoCycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MesoCycle
        fields = '__all__'


class EditMesoCycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MesoCycle
        fields = '__all__'


class DeleteMesoCycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MesoCycle
        fields = '__all__'


# =================  Micro Cycle Serializers ====================== #

class ListAllMicroCyclesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MicroCycle
        fields = '__all__'


class CreateMicroCycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MicroCycle
        fields = '__all__'


class EditMicroCycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MicroCycle
        fields = '__all__'


class DeleteMicroCycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MicroCycle
        fields = '__all__'
