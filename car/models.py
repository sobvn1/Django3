from django.db import models

class Car(models.Model):
    title = models.CharField(max_length=150)
    photo = models.ImageField(upload_to="")
    description = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    url_post = models.URLField(null=True)

    def __str__(self):
        return self.title



