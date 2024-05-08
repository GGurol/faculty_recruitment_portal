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

#Page 2 Model
class PageModel2(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phd_university = models.CharField(max_length=100)
    phd_department = models.CharField(max_length=100)
    phd_supervisor = models.CharField(max_length=100)
    phd_join_year = models.CharField(max_length=4)
    phd_defence_date = models.DateField()
    phd_award_date = models.DateField()
    phd_thesis_title = models.CharField(max_length=100)
    
    pg_degree = models.CharField(max_length=100)
    pg_university = models.CharField(max_length=100)
    pg_branch = models.CharField(max_length=100)
    pg_join_year = models.CharField(max_length=4)
    pg_completion_year = models.DateField()
    pg_duration = models.IntegerField()
    pg_percentage_cgpa = models.CharField(max_length=100)
    pg_division = models.CharField(max_length=100)

    ug_degree = models.CharField(max_length=100)
    ug_university = models.CharField(max_length=100)
    ug_branch = models.CharField(max_length=100)
    ug_join_year = models.CharField(max_length=4)
    ug_completion_year = models.DateField()
    ug_duration = models.IntegerField()
    ug_percentage_cgpa = models.CharField(max_length=100)
    ug_division = models.CharField(max_length=100)

    # Fields for School details
    college_class = models.CharField(max_length=100, blank=True, null=True)
    college_name = models.CharField(max_length=100, blank=True, null=True)
    college_passing_year = models.CharField(max_length=100, blank=True, null=True)
    college_percentage = models.CharField(max_length=100, blank=True, null=True)
    college_division = models.CharField(max_length=100, blank=True, null=True)
    school_class = models.CharField(max_length=100, blank=True, null=True)
    school_name = models.CharField(max_length=100, blank=True, null=True)
    school_passing_year = models.CharField(max_length=100, blank=True, null=True)
    school_percentage = models.CharField(max_length=100, blank=True, null=True)
    school_division = models.CharField(max_length=100, blank=True, null=True)

    # JSON field to store additional educational qualifications
    additional_qualifications = models.JSONField(default=list)

    class Meta:
        verbose_name = "Page 2 Model"
        verbose_name_plural = "Page 2 Models"


class PageModel3(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)
    organisation = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    joining_date = models.DateField()
    leaving_date = models.DateField()
    duration = models.IntegerField()
    area_of_specialization = models.TextField( blank=True, null=True)
    area_of_research = models.TextField( blank=True, null=True)
    class Meta:
        verbose_name = "Page 3 Model"
        verbose_name_plural = "Page 3 Models"

class PageModel4(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    international_journal_papers = models.IntegerField()
    national_journal_papers = models.IntegerField()
    international_conference_papers = models.IntegerField()
    national_conference_papers = models.IntegerField()
    patents = models.IntegerField()
    books = models.IntegerField()
    book_chapters = models.IntegerField()
    google_scholar_link = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = "Page 4 Model"
        verbose_name_plural = "Page 4 Models"

class PageModel5(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Define fields for Section 9
    # Membership of Professional Societies
    society_name = models.CharField(max_length=100)
    membership_status = models.CharField(max_length=20)

    # Define fields for Section 10
    # Professional Training
    training_type = models.CharField(max_length=100)
    training_organisation = models.CharField(max_length=100)
    training_year = models.CharField(max_length=4)
    training_durations = models.IntegerField()

    # Define fields for Section 11
    # Award(s) and Recognition(s)
    award_name = models.CharField(max_length=100)
    awarded_by = models.CharField(max_length=100)
    award_year = models.CharField(max_length=4)

    # Define fields for Section 12A
    # Sponsored Projects
    sponsored_agency = models.CharField(max_length=100)
    sponsored_title = models.CharField(max_length=100)
    sponsored_amount = models.CharField(max_length=100)
    sponsored_period = models.CharField(max_length=100)
    sponsored_role = models.CharField(max_length=100)
    sponsored_status = models.CharField(max_length=100)

    # Define fields for Section 12B
    # Consultancy Projects
    consultancy_organisation = models.CharField(max_length=100)
    consultancy_title = models.CharField(max_length=100)
    consultancy_amount = models.CharField(max_length=100)
    consultancy_period = models.CharField(max_length=100)
    consultancy_role = models.CharField(max_length=100)
    consultancy_status = models.CharField(max_length=100)

class PageModel6(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Define fields for Section 13
    # Research Supervision

    # (A) PhD Thesis Supervision
    phd_name = models.CharField(max_length=100)
    phd_title = models.CharField(max_length=100)
    phd_role = models.CharField(max_length=100)
    phd_status = models.CharField(max_length=100)
    phd_date = models.DateField()

    # (B) M.Tech/M.E./Master's Degree
    pg_name = models.CharField(max_length=100)
    pg_title = models.CharField(max_length=100)
    pg_role = models.CharField(max_length=100)
    pg_status = models.CharField(max_length=100)
    pg_date = models.DateField()

    # (C) B.Tech/B.E./Bachelor's Degree
    ug_name = models.CharField(max_length=100)
    ug_title = models.CharField(max_length=100)
    ug_role = models.CharField(max_length=100)
    ug_status = models.CharField(max_length=100)
    ug_date = models.DateField()

class PageModel7(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    research_plans = models.TextField(blank=True)
    teaching_plans = models.TextField(blank=True)
    other_details = models.TextField(blank=True)
    services_details = models.TextField(blank=True)
    jour_details = models.TextField(blank=True)
    conference_details = models.TextField(blank=True)

class PageModel8(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    research_papers = models.FileField(upload_to='research_papers')
    phd_certificate = models.FileField(upload_to='phd_certificate')
    pg_documents = models.FileField(upload_to='pg_documents')
    ug_documents = models.FileField(upload_to='ug_documents')
    certificate_12th = models.FileField(upload_to='certificate_12th')
    certificate_10th = models.FileField(upload_to='certificate_10th')
    pay_slip = models.FileField(upload_to='pay_slip')
    noc_undertaking = models.FileField(upload_to='noc_undertaking')
    post_phd_experience = models.FileField(upload_to='post_phd_experience')
    other_documents = models.FileField(upload_to='other_documents')
    signature = models.ImageField(upload_to='signature')

class Referee(models.Model):
    # page8 = models.ForeignKey(Page8, related_name='referees', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    association = models.CharField(max_length=100)
    organisation = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)


class PageModel9(models.Model):
    declaration_agreed = models.BooleanField(default=False)

    def __str__(self):
        return "Page Model 9"


class PersonalInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    photo = models.ImageField(upload_to='photos/')
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()
    nationality = models.CharField(max_length=100)
    category = models.CharField(max_length=10, choices=[('GEN', 'GEN'), ('EWS', 'EWS'), ('OBC', 'OBC'), ('SC', 'SC'), ('ST', 'ST'), ('PWD', 'PWD')])
    gender = models.CharField(max_length=20)
    marital_status = models.CharField(max_length=20, choices=[('Married', 'Married'), ('Single', 'Single')])
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    id_proof_type = models.CharField(max_length=100)
    id_proof_upload = models.FileField(upload_to='id_proofs/')
    street_correspondence = models.CharField(max_length=100)
    city_correspondence = models.CharField(max_length=100)
    district_correspondence = models.CharField(max_length=100)
    state_correspondence = models.CharField(max_length=100)
    country_correspondence = models.CharField(max_length=100)
    pin_correspondence = models.CharField(max_length=20)
    street_permanent = models.CharField(max_length=100)
    city_permanent = models.CharField(max_length=100)
    district_permanent = models.CharField(max_length=100)
    state_permanent = models.CharField(max_length=100)
    country_permanent = models.CharField(max_length=100)
    pin_permanent = models.CharField(max_length=20)
    mobile_number = models.CharField(max_length=15)
    alternate_mobile = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField()
    alternate_email = models.EmailField(blank=True, null=True)
    landline = models.CharField(max_length=15, blank=True, null=True)

class Education(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phd_university = models.CharField(max_length=100)
    phd_department = models.CharField(max_length=100)
    phd_supervisor = models.CharField(max_length=100)
    phd_join_year = models.PositiveIntegerField()
    phd_defence_date = models.DateField()
    phd_award_date = models.DateField()
    phd_thesis_title = models.CharField(max_length=100)
    pg_degree = models.CharField(max_length=100)
    pg_university = models.CharField(max_length=100)
    pg_branch = models.CharField(max_length=100)
    pg_join_year = models.PositiveIntegerField()
    pg_completion_year = models.DateField()
    pg_duration = models.PositiveIntegerField()
    pg_percentage_cgpa = models.DecimalField(max_digits=5, decimal_places=2)
    pg_division = models.CharField(max_length=100)
    ug_degree = models.CharField(max_length=100)
    ug_university = models.CharField(max_length=100)
    ug_branch = models.CharField(max_length=100)
    ug_join_year = models.PositiveIntegerField()
    ug_completion_year = models.DateField()
    ug_duration = models.PositiveIntegerField()
    ug_percentage_cgpa = models.DecimalField(max_digits=5, decimal_places=2)
    ug_division = models.CharField(max_length=100)

class Address(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    street_correspondence = models.CharField(max_length=100)
    city_correspondence = models.CharField(max_length=100)
    district_correspondence = models.CharField(max_length=100)
    state_correspondence = models.CharField(max_length=100)
    country_correspondence = models.CharField(max_length=100)
    pin_correspondence = models.CharField(max_length=20)
    street_permanent = models.CharField(max_length=100)
    city_permanent = models.CharField(max_length=100)
    district_permanent = models.CharField(max_length=100)
    state_permanent = models.CharField(max_length=100)
    country_permanent = models.CharField(max_length=100)
    pin_permanent = models.CharField(max_length=20)

class Employment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)
    organisation = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    joining_date = models.DateField()
    leaving_date = models.DateField()
    duration = models.PositiveIntegerField()
    area_of_specialization = models.TextField(blank=True, null=True)
    area_of_research = models.TextField(blank=True, null=True)

class Publication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    international_journal_papers = models.PositiveIntegerField()
    national_journal_papers = models.PositiveIntegerField()
    international_conference_papers = models.PositiveIntegerField()
    national_conference_papers = models.PositiveIntegerField()
    patents = models.PositiveIntegerField()
    books = models.PositiveIntegerField()
    book_chapters = models.PositiveIntegerField()
    google_scholar_link = models.URLField(max_length=200, blank=True)

class Achievements(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    society_name = models.CharField(max_length=100)
    membership_status = models.CharField(max_length=20)
    training_type = models.CharField(max_length=100)
    training_organisation = models.CharField(max_length=100)
    training_year = models.PositiveIntegerField()
    training_durations = models.PositiveIntegerField()
    award_name = models.CharField(max_length=100)
    awarded_by = models.CharField(max_length=100)
    award_year = models.PositiveIntegerField()
    sponsored_agency = models.CharField(max_length=100)
    sponsored_title = models.CharField(max_length=100)
    sponsored_amount = models.CharField(max_length=100)
    sponsored_period = models.CharField(max_length=100)
    sponsored_role = models.CharField(max_length=100)
    sponsored_status = models.CharField(max_length=100)
    consultancy_organisation = models.CharField(max_length=100)
    consultancy_title = models.CharField(max_length=100)
    consultancy_amount = models.CharField(max_length=100)
    consultancy_period = models.CharField(max_length=100)
    consultancy_role = models.CharField(max_length=100)
    consultancy_status = models.CharField(max_length=100)

class Supervision(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phd_name = models.CharField(max_length=100)
    phd_title = models.CharField(max_length=100)
    phd_role = models.CharField(max_length=100)
    phd_status = models.CharField(max_length=100)
    phd_date = models.DateField()
    pg_name = models.CharField(max_length=100)
    pg_title = models.CharField(max_length=100)
    pg_role = models.CharField(max_length=100)
    pg_status = models.CharField(max_length=100)
    pg_date = models.DateField()
    ug_name = models.CharField(max_length=100)
    ug_title = models.CharField(max_length=100)
    ug_role = models.CharField(max_length=100)
    ug_status = models.CharField(max_length=100)
    ug_date = models.DateField()

class Plans(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    research_plans = models.TextField(blank=True)
    teaching_plans = models.TextField(blank=True)
    other_details = models.TextField(blank=True)
    services_details = models.TextField(blank=True)
    jour_details = models.TextField(blank=True)
    conference_details = models.TextField(blank=True)

class PDFFiles(models.Model):
    title=models.CharField(max_length=100)
    file=models.FileField(upload_to='files')