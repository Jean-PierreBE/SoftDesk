from rest_framework import serializers

from tracking import models

class ProjectCreateSerializer(serializers.ModelSerializer):
    """
    Serializer to Add Contributor together with Project
    """

    class ContributorSerializer(serializers.ModelSerializer):
        class Meta:
            model = models.Contributor
            fields = ('id', 'role')

    model_c = ContributorSerializer()

    class Meta:
        model = models.Project
        fields = '__all__'

    def create(self, validated_data):
        model_c_data = validated_data.pop('model_c')
        model_a_instance = models.Project.objects.create(**validated_data)
        models.Contributor.objects.create(project=model_a_instance,
                              **model_c_data)
        return model_a_instance