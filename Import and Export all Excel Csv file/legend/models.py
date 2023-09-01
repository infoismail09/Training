from django.db import models


class Country(models.Model):
    short_name = models.CharField(max_length=3, null=True)
    name = models.CharField(max_length=50)
    country_code = models.CharField(max_length=6, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "legend_country"
        verbose_name = "Country"
        verbose_name_plural = "Countries"
            

class State(models.Model):
    name = models.CharField(max_length=50)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "legend_state"
        

class City(models.Model):
    name = models.CharField(max_length=50)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "legend_city"
        verbose_name = "City"
        verbose_name_plural = "Cities"
        
