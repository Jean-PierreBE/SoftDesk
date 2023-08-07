from rest_framework import serializers

from tracking.models import Project, Contributor

class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        exclude = ('project',)

class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = "__all__"
