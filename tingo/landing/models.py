from django.db import models

# Create your models here.


class ImageProfile(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)
    sexo = models.CharField()
    bio = models.TextField()
    imagen = models.ImageField(upload_to=user_directory_path)
