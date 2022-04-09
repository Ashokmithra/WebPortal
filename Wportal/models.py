from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('Null', 'Null'),
        ('Student', 'Student'),
        ('Teacher', 'Teacher')
    )
    user_type = models.CharField(
        max_length=10, choices=USER_TYPE_CHOICES, default=0)

    def serialize(self):
        return{
            "name": self.username,
            "email": self.email,
            "id": self.id
        }


class Teacher(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="tusers")
    qualify = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    experince = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username


class Student(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="susers")
    standard = models.CharField(max_length=100)
    dob = models.CharField(max_length=100)
    age = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.user.username


class Note(models.Model):
    SUBJECT_CHOICE = (
        ('Select', 'Select'),
        ('Tamil', 'Tamil'),
        ('English', 'English'),
        ('Maths', 'Maths'),
        ('Science', 'Science'),
        ('Social Science', 'Social Science')
    )
    STANDARD_CHOICE = (
        ('Select', 'Select'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10')
    )
    title = models.CharField(max_length=100)
    subject = models.CharField(
        max_length=100, choices=SUBJECT_CHOICE, default=0)
    standard = models.CharField(
        max_length=100, choices=STANDARD_CHOICE, default=0)
    pdf = models.FileField()
    unit = models.CharField(
        max_length=100, choices=STANDARD_CHOICE, default="")

    def serialize(self):
        return{
            "subject": self.subject,
            "title": self.title,
            "standard": self.standard,
            "pdf": self.pdf.url,
            "unit": self.unit
        }

    def __str__(self):
        return self.subject
