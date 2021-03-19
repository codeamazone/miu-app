from django.db import models
from django.urls import reverse


class Idea(models.Model):
    PENDING = 'Pending'
    ONGOING = 'In Progress'
    COMPLETED = 'Completed'

    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (ONGOING, 'In progress'),
        (COMPLETED, 'Completed')
    ]

    VISION = 'Vision'
    TRY_SOMETHING = 'Try something'
    PROJECT = 'Project'

    KIND_CHOICES = [
        (VISION, 'Vision'),
        (TRY_SOMETHING, 'Try something'),
        (PROJECT, 'Project')
    ]

    idea = models.CharField(max_length=200)
    kind = models.CharField(
        max_length=15,
        choices=KIND_CHOICES,
        default=VISION
    )
    description = models.TextField()
    next_steps = models.TextField(null=True)
    status = models.CharField(
        max_length=11,
        choices=STATUS_CHOICES,
        default=PENDING
    )

    def __str__(self):
        return self.idea

    def get_absolute_url(self):
        return reverse('idea_detail', args=[str(self.id)])


# Write tests
# TODO: create Todos model connected to next_steps from ideas model
