from django.db import models
from django.conf import settings

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=55, verbose_name="Titre")
    description = models.TextField(max_length=2048, blank=True, verbose_name="Description du projet")
    type = models.CharField(max_length=55, verbose_name="Type de projet")


class Contributor(models.Model):
    ROLES = (
        ('PM', 'Project Manager'),
        ('DEV', 'Developer'),
        ('TST', 'Tester'),
        ('OWN', 'Business Owner'),
        ('AN', 'Analyst'),
    )
    GRANTS = (
        ('RO', 'Read Only'),
        ('WT', 'Write'),
    )

    permission = models.CharField(max_length=55, choices=GRANTS, verbose_name="Droits accordés")
    role = models.CharField(max_length=55, choices=ROLES, verbose_name="Rôle")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, default=None)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Issue(models.Model):
    title = models.CharField(max_length=55, verbose_name="Titre issue")
    description = models.TextField(max_length=2048, blank=True, verbose_name="Description de l'issue")
    tag = models.CharField(max_length=55, verbose_name="Tag")
    priority = models.CharField(max_length=55, verbose_name="Priorité")
    status = models.CharField(max_length=55, verbose_name="Statut")
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE)
    author_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
                                    null=True, related_name='creator')
    assignee_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
                                      null=True, related_name='assign')
    time_created = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    description = models.TextField(max_length=2048, blank=True, verbose_name="Commentaire")
    issue = models.ForeignKey(to=Issue, on_delete=models.CASCADE)
    author_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    time_created = models.DateTimeField(auto_now_add=True)
