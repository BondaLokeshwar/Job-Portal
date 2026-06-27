from django.db import models
from django.contrib.auth.models import User


# Employer Profile
class Employer(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    company_name = models.CharField(
        max_length=200
    )

    first_name = models.CharField(
        max_length=100
    )

    last_name = models.CharField(
        max_length=100
    )

    phone = models.CharField(
        max_length=15
    )

    website = models.URLField(
        blank=True
    )

    company_description = models.TextField(
        blank=True
    )

    company_logo = models.ImageField(
        upload_to="company_logos/",
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.company_name
    
# Candidate Profile
class CandidateProfile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    phone = models.CharField(
        max_length=15
    )

    address = models.TextField()

    skills = models.TextField()

    education = models.CharField(
        max_length=200
    )

    experience = models.CharField(
        max_length=100
    )

    resume = models.FileField(
        upload_to="resumes/",
        blank=True,
        null=True
    )

    profile_image = models.ImageField(
        upload_to="profile_images/",
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.user.first_name
# Job Model
class Job(models.Model):
    employer = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    salary = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    job_type = models.CharField(max_length=100)
    description = models.TextField()
    skills = models.TextField()
    deadline = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
# Application Model
class Application(models.Model):

    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE
    )

    candidate_name = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    email = models.EmailField(
        blank=True,
        null=True
    )

    phone = models.CharField(
        max_length=15,
        blank=True,
        null=True
    )

    education = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )

    skills = models.TextField(
        blank=True,
        null=True
    )

    resume = models.FileField(
        upload_to='resumes/',
        blank=True,
        null=True
    )

    cover_letter = models.TextField(
        blank=True,
        null=True
    )

    applied_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.candidate_name} - {self.job.title}"