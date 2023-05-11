from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Profile(models.Model):
    userid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phno = models.CharField(max_length=10)
    acct_creation = models.DateTimeField(default=timezone.now)
    profile_picture = models.ImageField(upload_to='profile_pictures/')
    active_user = models.BooleanField()
    
    def activate(self):
        self.acct_creation = timezone.now()
        self.save()

    def __str__(self):
        return self.userid
    
GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    )
LEVEL_OF_STUDY = (
        ('Graduate', 'MASTERS'),
        ('Graduate', 'PHD'),
        ('Undergraduate', 'BACHELORS')
    )
COLLEGE = (
        ('College of Information and Sciences', 'CICS'),
        ('Other', 'other')
)
YEAR = (
        ('Freshman', 'Freshman'),
        ('Sophomore', 'Sophomore'),
        ('Junior', 'Junior'),
        ('Senior', 'Senior'),
        ('NA', 'NA')
)
MAJOR = (
        ('Computer Science', 'Computer Science'),
        ('Data Science', 'Data Science'),
        ('Accounting', 'Accounting'),
        ('Pyschology', 'Pyschology'),
        ('Undecided', 'Undecided')
)
SLEEP_HABITS = (
        ('Before 9pm', 'Before 9pm'),
        ('Before 11pm', 'Before 9pm'),
        ('Before 1am', 'Before 1am')
)

class Preferences(models.Model):
    userid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    gender = models.CharField(max_length=25, choices=GENDER_CHOICES)
    level_of_study = models.CharField(max_length=25, choices=LEVEL_OF_STUDY)
    college = models.CharField(max_length=35, choices=COLLEGE)
    major = models.CharField(max_length=25, choices=MAJOR)
    sleep_habits = models.CharField(max_length=25, choices=SLEEP_HABITS)