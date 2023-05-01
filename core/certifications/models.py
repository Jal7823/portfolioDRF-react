from django.db import models


class Certifications(models.Model):
    """Should created a model for certifications."""

    name = models.CharField("Name", max_length=50)
    institutions = models.CharField("Institutions", max_length=100)
    image = models.ImageField("Image", upload_to="certf", null=True, blank=True)
    url = models.URLField()
    created = models.DateTimeField("Creation", auto_now_add=True)
    updated = models.DateTimeField("Updated", auto_now_add=True)

    class Meta:
        """Meta definition for Cerfications."""

        verbose_name = "Cerfications"
        verbose_name_plural = "Cerficationss"

    def __str__(self):
        """Unicode representation of Cerfications."""
        return self.name
