from django.db import models

class home(models.Model):
    title = models.CharField(max_length = 300)
    hero_img = models.ImageField(blank=False)

    def __str__(self):
        return self.title