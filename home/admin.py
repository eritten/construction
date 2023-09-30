from django.contrib import admin
from .models import Application, Member, NewsLetter 
# Register your models here.
# available_positions, full_name, email, phone_number, address, highest_level_of_education school_university_name, degree_earned year_of_graduation previous_job_title  dates_employed  relevant_certifications computer_skills  reference1_name reference1_phone_number reference1_email  reference2_name reference2_phone_number reference2_email how_did_you_hear_about_us why_do_you_want_to_work_for_us resume cover_letter date form_id
# create a class for the model to be displayed in the admin panel

class ApplicationAdmin(admin.ModelAdmin):
    list_display= ['full_name', 'email', 'phone_number', 'address', 'highest_level_of_education', 'school_university_name', 'degree_earned', 'year_of_graduation', 'previous_job_title', 'dates_employed', 'relevant_certifications', 'computer_skills', 'reference1_name', 'reference1_phone_number', 'reference1_email', 'reference2_name', 'reference2_phone_number', 'reference2_email', 'how_did_you_hear_about_us', 'why_do_you_want_to_work_for_us', 'resume', 'cover_letter', 'date', 'form_id']
    list_filter = ['full_name', 'email', 'phone_number', 'address', 'highest_level_of_education', 'school_university_name', 'degree_earned', 'year_of_graduation', 'previous_job_title', 'dates_employed', 'relevant_certifications', 'computer_skills', 'reference1_name', 'reference1_phone_number', 'reference1_email', 'reference2_name', 'reference2_phone_number', 'reference2_email', 'how_did_you_hear_about_us', 'why_do_you_want_to_work_for_us', 'resume', 'cover_letter', 'date', 'form_id']
    search_fields = ['full_name', 'email', 'phone_number', 'address', 'highest_level_of_education', 'school_university_name', 'degree_earned', 'year_of_graduation', 'previous_job_title', 'dates_employed', 'relevant_certifications', 'computer_skills', 'reference1_name', 'reference1_phone_number', 'reference1_email', 'reference2_name', 'reference2_phone_number', 'reference2_email', 'how_did_you_hear_about_us', 'why_do_you_want_to_work_for_us', 'resume', 'cover_letter', 'date', 'form_id']
    list_per_page = 25
    
    
admin.site.register(Application, ApplicationAdmin)


admin.site.site_header = "Halleluya properties limited admin Panel"
admin.site.site_title = "Halleluya properties limited admin Panel"
admin.site.index_title = "Welcome to Halleluya properties limited admin Panel"



class MemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
    list_filter = ['name', 'email']
    search_fields = ['name', 'email']
    list_per_page = 25
    
admin.site.register(Member, MemberAdmin)


class NewsLetterAdmin(admin.ModelAdmin):
    list_display = ['title', 'content']
    list_filter = ['title', 'content']
    search_fields = ['title', 'content']
    list_per_page = 25
    
admin.site.register(NewsLetter, NewsLetterAdmin)