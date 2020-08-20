# Dango imports
from django.db import models


class Post(models.Model):
    """
    Model Post.
    """
    title = models.CharField(verbose_name='título', max_length=100)
    description = models.TextField(verbose_name='descrição')
    image_url = models.URLField()

    created_by = models.ForeignKey(
        'user.User', on_delete=models.CASCADE, verbose_name='criado por'
    )
    created_at = models.DateTimeField(
        verbose_name='Criado em', auto_now_add=True
    )
    modified_at = models.DateTimeField(
        verbose_name='Modificado em', auto_now=True
    )

    class Meta:
        """
        Meta model class
        Defines the displayed singular and plural name of the model
        """
        verbose_name = "post"
        verbose_name_plural = "posts"

    def __str__(self):
        """ Returns the post title. """
        return self.title