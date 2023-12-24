from django.db import models


class Pais(models.Model):
    name_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Barrio(models.Model):
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    name_text = models.CharField(max_length=200)
    