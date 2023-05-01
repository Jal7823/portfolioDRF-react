from django.db import models
from ..skills.models import Language,Library

class Projects(models.Model):
    name = models.CharField('Project',max_length=200)
    description = models.TextField('Description',max_length=500)
    image = models.ImageField('Image',upload_to='projects',null=True,blank=True)
    language = models.ManyToManyField(Language,related_name='Library')
    github = models.URLField('GitHub',null=True,blank=True)
    link = models.URLField('Link',null=True,blank=True)
    created = models.DateTimeField('Creation',auto_now_add=True)
    updated = models.DateTimeField('Updated',auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Projects'
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'