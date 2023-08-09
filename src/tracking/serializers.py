from rest_framework import serializers

from tracking.models import Project, Contributor

class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = "__all__"

class ContributorSerializer(serializers.ModelSerializer):
    #project = ProjectSerializer()
    class Meta:
        model = Contributor
        fields = "__all__"

class ProjectDetailSerializer(serializers.ModelSerializer):
    contributor_set = ContributorSerializer(many=True)
    class Meta:
        model = Project
        fields = "__all__"

