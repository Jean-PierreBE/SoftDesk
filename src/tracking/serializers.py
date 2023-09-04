from rest_framework import serializers
from django.db.models import Q
from tracking.models import Project, Contributor, Issue, Comment


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = "__all__"


class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = "__all__"


class ContributorUpdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = ['id', 'role']

    def validate(self, data):
        my_view = self.context['view']
        object_id = my_view.kwargs.get('project_id')
        creator = Contributor.objects.filter(Q(role='CRT') & Q(project_id=object_id))
        if creator.exists() and data['role'] == 'CRT':
            raise serializers.ValidationError('A creator exists allready!!')
        return data


class ProjectDetailSerializer(serializers.ModelSerializer):
    contributor_set = ContributorSerializer(many=True)

    class Meta:
        model = Project
        fields = "__all__"


class IssueSerializer(serializers.ModelSerializer):

    class Meta:
        model = Issue
        fields = "__all__"


class IssueUpdSerializer(serializers.ModelSerializer):

    class Meta:
        model = Issue
        fields = ['id', 'title', 'description', 'tag', 'priority', 'status', 'assignee_user']

    def validate(self, data):

        my_view = self.context['view']
        object_id = my_view.kwargs.get('project_id')
        user_ok = Contributor.objects.filter(Q(author_user=data['assignee_user']) & Q(project_id=object_id))
        if user_ok.exists():
            if data['assignee_user'] == self.context["request"].user:
                raise serializers.ValidationError('assignee_user should be different from author_user!!')
        else:
            raise serializers.ValidationError('assignee_user doesn''t belong to the project!!')
        return data


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = "__all__"


class CommentUpdSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['id', 'description']
