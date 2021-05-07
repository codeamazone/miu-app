from django.db import models
from django.urls import reverse


class IdeaStatus(models.IntegerChoices):
    PENDING = 0, 'Pending'
    ONGOING = 1, 'In progress'
    COMPLETED = 2, 'Completed'


class IdeaKind(models.IntegerChoices):
    VISION = 0, 'Vision'
    TRY_SOMETHING = 1, 'Try something'
    PROJECT = 2, 'Project'


class Idea(models.Model):
    idea = models.CharField(max_length=200)
    kind = models.IntegerField(
        default=IdeaKind.VISION,
        choices=IdeaKind.choices
    )
    description = models.TextField()
    next_steps = models.TextField(null=True)
    status = models.IntegerField(
        default=IdeaStatus.PENDING,
        choices=IdeaStatus.choices
    )

    def __str__(self):
        return self.idea

    def get_absolute_url(self):
        return reverse('idea_detail', args=[str(self.id)])


# TODO: Write tests
