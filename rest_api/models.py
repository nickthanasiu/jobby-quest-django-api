from django.db import models

# Create your models here.

class Job(models.Model):
    SAFETY = 's'
    BALLPARK = 'b'
    REACH = 'r'

    PROSPECT_RATING_CHOICES = (
        (SAFETY, 'safety'),
        (BALLPARK, 'ballpark'),
        (REACH, 'reach')
    )

    INTEREST_RATING_CHOICES = (
        ('low', 1),
        ('medium', 2),
        ('high', 3)
    )

    url = models.URLField(max_length = 250)
    company = models.CharField(max_length = 50)
    job_title = models.CharField(max_length = 50)
    user_interest_rating = models.IntegerField(
        choices = INTEREST_RATING_CHOICES,
        default = 3
    )
    user_prospect_rating = models.CharField(
        max_length = 1,
        choices = PROSPECT_RATING_CHOICES,
    )
    img_url = models.URLField(max_length = 250)