from django.db import models
# importing validators to accept pdf and doc files
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError

# Create your models here.


class Application(models.Model):
    JOB_POSITIONS = (
            ('Bricklayers and masons', 'Bricklayers and masons'),
            ('Roofers, roof tilers and slaters', 'Roofers, roof tilers and slaters'),
            ('Carpenters and joiners', 'Carpenters and joiners'),
            ('Construction and building trades', 'Construction and building trades'),
            ('Plasterers including dry liners', 'Plasterers including dry liners'),
            ('Floorers and wall tilers', 'Floorers and wall tilers'),
        )     
    available_positions = models.CharField(max_length=100, choices=JOB_POSITIONS)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    highest_level_of_education = models.CharField(max_length=100)
    school_university_name = models.CharField(max_length=100)
    degree_earned = models.CharField(max_length=100)
    year_of_graduation = models.CharField(max_length=100)
    previous_job_title = models.CharField(max_length=100)
    dates_employed = models.CharField(max_length=100)
    responsibilities = models.TextField()
    relevant_certifications = models.TextField()
    computer_skills = models.TextField()
    reference1_name = models.CharField(max_length=100)
    reference1_phone_number = models.CharField(max_length=100)
    reference1_email = models.EmailField()
    reference2_name = models.CharField(max_length=100)
    reference2_phone_number = models.CharField(max_length=100)
    reference2_email = models.EmailField()
    how_did_you_hear_about_us = models.CharField(max_length=100)
    why_do_you_want_to_work_for_us = models.TextField()
    resume = models.FileField(upload_to='resumes/', validators=[FileExtensionValidator(['pdf', 'doc'])  ])
    cover_letter = models.FileField(upload_to='cover_letters/', validators=[FileExtensionValidator(['pdf', 'doc', 'jpg', 'png'])])
    signature = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    form_id = models.CharField(max_length=100)
    def __str__(self):
        return self.full_name
    
 