from django.db import models

from Petstagram.photos.models import Photo


class Comment(models.Model):
    class Meta:
        indexes = [
            models.Index(fields=['datetime_of_publication'])
        ]
        ordering = ['-datetime_of_publication']

    text = models.TextField(
        max_length=300,
    )

    datetime_of_publication = models.DateTimeField(
        auto_now_add=True,
    )

    to_photo = models.ForeignKey(
        to=Photo,
        on_delete=models.CASCADE,
    )


class Like(models.Model):
    to_photo = models.ForeignKey(
        to=Photo,
        on_delete=models.CASCADE,
    )

