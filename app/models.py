# models.py

from django.db import models
from django.contrib.auth.models import User

class UserRegistration(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    category = models.CharField(max_length=10, choices=[('GEN', 'GEN'), ('EWS', 'EWS'), ('OBC', 'OBC'), ('SC', 'SC'), ('ST', 'ST'), ('PWD', 'PWD')])
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.email

class PageModel1(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    advertisement_number = models.CharField(max_length=100)
    post_applied_for = models.CharField(max_length=100)
    date_of_application = models.DateField()
    application_number = models.CharField(max_length=20)
    department = models.CharField(max_length=100)

    # Personal Details
    photo = models.ImageField(upload_to='photos/')
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()
    nationality = models.CharField(max_length=100)
    category = models.CharField(max_length=10, choices=[('GEN', 'GEN'), ('EWS', 'EWS'), ('OBC', 'OBC'), ('SC', 'SC'), ('ST', 'ST'), ('PWD', 'PWD')])
    gender = models.CharField(max_length=20)
    marital_status = models.CharField(max_length=20,choices=[('Married', 'Married'), ('Single', 'Single')])
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    id_proof_type = models.CharField(max_length=100)
    id_proof_upload = models.FileField(upload_to='id_proofs/')

    # Correspondence Address
    street_correspondence = models.CharField(max_length=100)
    city_correspondence = models.CharField(max_length=100)
    district_correspondence = models.CharField(max_length=100)
    state_correspondence = models.CharField(max_length=100)
    country_correspondence = models.CharField(max_length=100)
    pin_correspondence = models.CharField(max_length=20)

    # Permanent Address
    street_permanent = models.CharField(max_length=100)
    city_permanent = models.CharField(max_length=100)
    district_permanent = models.CharField(max_length=100)
    state_permanent = models.CharField(max_length=100)
    country_permanent = models.CharField(max_length=100)
    pin_permanent = models.CharField(max_length=20)

    # Contact Details
    mobile_number = models.CharField(max_length=15)
    alternate_mobile = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField()
    alternate_email = models.EmailField(blank=True, null=True)
    landline = models.CharField(max_length=15, blank=True, null=True)

