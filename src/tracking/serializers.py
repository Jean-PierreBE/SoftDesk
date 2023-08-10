from rest_framework import serializers

from tracking.models import Project, Contributor, Issue, Comment

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

class IssueSerializer(serializers.ModelSerializer):

    class Meta:
        model = Issue
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = "__all__"
