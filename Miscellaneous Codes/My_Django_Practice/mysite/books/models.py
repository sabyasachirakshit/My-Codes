from django.db import models
# Create your models here.



class Publishers(models.Model):
    name = models.CharField(max_length=30)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=30)
    website = models.URLField()

    def __str__(self):
        return f"{self.name},{self.country}"

    class Meta:
        ordering = ["name"]



class Authors(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email_address = models.EmailField()

    def __str__(self):
        return f"{self.firstname},{self.lastname}"



class Books(models.Model):
    title = models.CharField(max_length=50)
    publication_date = models.DateField()
    authors = models.ManyToManyField(Authors)
    publishers = models.ForeignKey(Publishers)

    def __str__(self):
        return self.title
