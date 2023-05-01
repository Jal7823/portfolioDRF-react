from django.db import models

class Library(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField('Image',upload_to='logos',null=True,blank=True)
    icon = models.CharField('Icon',max_length=100,null=True,blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Library'
        verbose_name = 'Library'
        verbose_name_plural = 'Libraries'

class Language(models.Model):
    name = models.CharField(max_length=100,verbose_name='Language')
    image = models.ImageField('Image',upload_to='skills',null=True,blank=True)
    library = models.ManyToManyField(Library)
    icon = models.CharField('Icon',max_length=100,null=True,blank=True)


    def __str__(self):
        return self.name


    class Meta:
        db_table = 'Language'
        verbose_name = 'Language'
        verbose_name_plural = 'Languages'