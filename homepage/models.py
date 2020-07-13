from django.db import models

class homepageinfo(models.Model):
    title = models.CharField(max_length=40)
    subtitle = models.CharField(max_length=40)
    banner = models.ImageField()
    date_updated = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.date_updated)
    


