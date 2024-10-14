from django.db import models
from django.template.defaultfilters import slugify

from Petstagram.photos.validators import FileSizeValidator


class Pet(models.Model):
    name = models.CharField(
        max_length=30,
    )

    personal_photo = models.URLField()

    date_of_birth = models.DateField(
        blank=True,
        null=True,
    )

    slug = models.SlugField(
        unique=True,
        null=True,
        blank=True,
        editable=False,
    )

    def save(self, *args, **kwargs):

        super().save(*args, **kwargs)  # to save the object in the database
        """
        if self.name, self.id is 'Sasho Petkov' 2 it will slugify it to sasho-petkov-2 (where 2 is the id).
        """
        if not self.slug:
            self.slug = slugify(f"{self.name}-{self.id}")

        super().save(*args, **kwargs)  # to save new data of the slug

    def __str__(self):
        return self.name
