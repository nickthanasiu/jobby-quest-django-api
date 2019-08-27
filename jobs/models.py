from django.db import models

# Create your models here.

class Job(models.Model):
    SAFETY = 'safety'
    BALLPARK = 'ballpark'
    REACH = 'reach'

    PROSPECT_RATING_CHOICES = (
        (SAFETY, 'safety'),
        (BALLPARK, 'ballpark'),
        (REACH, 'reach')
    )

    INTEREST_RATING_CHOICES = (
        (1, 1),
        (2, 2),
        (3, 3)
    )

    url = models.URLField(max_length = 250)
    company = models.CharField(max_length = 50)
    job_title = models.CharField(max_length = 50)
    user_interest_rating = models.IntegerField(
        choices = INTEREST_RATING_CHOICES,
        default = 3,
        blank=True
    )

    user_prospect_rating = models.CharField(
        max_length = 10,
        choices = PROSPECT_RATING_CHOICES,
        default=BALLPARK,
        blank=True
    )

    img_url = models.URLField(max_length = 250)

    def __str__(self):
        return (self.company + ' - ' + self.job_title) 