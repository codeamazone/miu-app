from django.db import models
from django.urls import reverse


class Idea(models.Model):
    PENDING = 'NO'
    ONGOING = 'ON'
    COMPLETED = 'OK'

    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (ONGOING, 'In Progress'),
        (COMPLETED, 'Completed')
    ]

    VISION = 'VIS'
    TRY_SOMETHING = 'TRY'
    PROJECT = 'PRO'

    KIND_CHOICES = [
        (VISION, 'Vision'),
        (TRY_SOMETHING, 'Try something'),
        (PROJECT, 'Project')
    ]

    idea = models.CharField(max_length=200)
    kind = models.CharField(
        max_length=3,
        choices=KIND_CHOICES,
        default=VISION
    )
    description = models.TextField()
    next_steps = models.TextField(null=True)
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default=PENDING
    )

    def __str__(self):
        return self.idea

    def get_absulute_url(self):
        return reverse('idea_detail', args=[str(self.id)])


# TODO: create Todos model connected to next_steps from ideas model
