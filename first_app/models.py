from django.db import models
from django_countries.fields import CountryField
# from phonenumber_field.modelfields import PhoneNumberField

# Candidate profile description


class Profile(models.Model):
    profiles = models.Manager()
    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20, blank=True)
    birth_date = models.DateField(default=None)
    country = CountryField()
    # gender = models.CharField(max_length=1)
    address = models.CharField(max_length=40, blank=True, default=None)
    email = models.EmailField(max_length=40, blank=True, default=None)
    # phone_number = PhoneNumberField()
    linkedIn = models.URLField(blank=True, default=None, null=True)
    isAvailableNow = models.BooleanField(max_length=2, default=False)
    # noticePeriod = models.CharField(max_length=2, default=None)
    salary = models.IntegerField(default=None, blank=True, null=True)
    # creation_date = models.DateField()
    # cv
    # current employer

    def __str__(self):
        return self.first_name + self.last_name

# Role description


class Role(models.Model):
    role_name = models.CharField(max_length=20, blank=True)  # cv role NAME
    role_class = models.CharField(max_length=20, blank=True, default=None)
    role_industry = models.CharField(max_length=20, blank=True, default=None)
    role_description = models.CharField(max_length=264, blank=True, default=None)

    def __str__(self):
        return self.role_name

# Profile Skill Description


class Skill(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=20, blank=True)
    # keyword
    rating = models.IntegerField(blank=True, default=None)  # estimated rating following quiz
    client_rating = models.IntegerField(blank=True, default=None)  # rating based on client feedback
    years = models.FloatField(default=None, blank=True)  # effective nb years of practice
    metric1 = models.IntegerField(blank=True, default=None)
    metric2 = models.IntegerField(blank=True, default=None)

    def __str__(self):
        return self.profile + self.language + self.rating


class Hobbie(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    hobbie_name = models.CharField(max_length=20, blank=False)
    hobbie_description = models.CharField(max_length=264, blank=True, default=None)

    def __str__(self):
        return self.profile + self.hobbie_name


# Profile Experience
class Experience(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    client_name = models.CharField(max_length=20, blank=True, default=None)
    # industry
    start_date = models.DateField(default=None, blank=True)
    end_date = models.DateField(default=None, blank=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, default=None)
    # metrics
    client_feedback = models.CharField(max_length=2, blank=True, default=None)
    # grade based on client feedback
    client_note = models.IntegerField(blank=True, default=None)

    def __str__(self):
        return self.client_name + " from " + str(self.start_date) + " to " + str(object=self.end_date)

# Keyword used for search


class Keyword(models.Model):
    keyword_name = models.CharField(max_length=20, blank=True, default=None)

# Client description


class Client(models.Model):
    client_name = models.CharField(max_length=30, blank=True, default=None)
    # contact =
    address = models.CharField(max_length=40, blank=True, default=None)
    # phone_number
    email = models.EmailField(max_length=40, blank=True, default=None)

    def __str__(self):
        return self.client_name


class Job(models.Model):
    title = models.CharField(max_length=30, blank=True, default=None)
    description = models.CharField(max_length=264, blank=True, default=None)
    start_date = models.DateField(default=None, blank=True)
    end_date = models.DateField(default=None, blank=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    salary = models.IntegerField(default=None)

    def __str__(self):
        return self.title

# Application Parameters


class Parameter(models.Model):
    name = models.CharField(max_length=20, blank=True)
    value = models.CharField(max_length=20, blank=True)
