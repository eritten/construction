from django.contrib import admin
from django.core.mail import send_mail
from .models import Application, Member, NewsLetter 
# Register your models here.
# available_positions, full_name, email, phone_number, address, highest_level_of_education school_university_name, degree_earned year_of_graduation previous_job_title  dates_employed  relevant_certifications computer_skills  reference1_name reference1_phone_number reference1_email  reference2_name reference2_phone_number reference2_email how_did_you_hear_about_us why_do_you_want_to_work_for_us resume cover_letter date form_id
# create a class for the model to be displayed in the admin panel

class ApplicationAdmin(admin.ModelAdmin):
    list_display= ['full_name', 'email', 'phone_number', 'address', 'highest_level_of_education', 'school_university_name', 'degree_earned', 'year_of_graduation', 'previous_job_title', 'dates_employed', 'relevant_certifications', 'computer_skills', 'reference1_name', 'reference1_phone_number', 'reference1_email', 'reference2_name', 'reference2_phone_number', 'reference2_email', 'how_did_you_hear_about_us', 'why_do_you_want_to_work_for_us', 'resume', 'cover_letter', 'date', 'form_id']
    list_filter = ['full_name', 'email', 'phone_number', 'address', 'highest_level_of_education', 'school_university_name', 'degree_earned', 'year_of_graduation', 'previous_job_title', 'dates_employed', 'relevant_certifications', 'computer_skills', 'reference1_name', 'reference1_phone_number', 'reference1_email', 'reference2_name', 'reference2_phone_number', 'reference2_email', 'how_did_you_hear_about_us', 'why_do_you_want_to_work_for_us', 'resume', 'cover_letter', 'date', 'form_id']
    search_fields = ['full_name', 'email', 'phone_number', 'address', 'highest_level_of_education', 'school_university_name', 'degree_earned', 'year_of_graduation', 'previous_job_title', 'dates_employed', 'relevant_certifications', 'computer_skills', 'reference1_name', 'reference1_phone_number', 'reference1_email', 'reference2_name', 'reference2_phone_number', 'reference2_email', 'how_did_you_hear_about_us', 'why_do_you_want_to_work_for_us', 'resume', 'cover_letter', 'date', 'form_id']
    list_per_page = 25
    # adding action to application admin for accepting and rejecting applications
    actions = ['accept_application', 'reject_application']
    # creating a function to accept application
    # def accept_application(self, request, queryset):
    #     queryset.update(status='Accepted')
    # accept_application.short_description = "Accept Application"
    # send an email to the applicant
    def accept_application(self, request, queryset):
#        queryset.update(status='Accepted')
        full_name = queryset.values('full_name')
        email = queryset.email
        send_mail(
            "Application Accepted",
            f"Dear {full_name},\nYour application has been accepted. We will get back to you soon.",
            'info@halleluyapropertieslimited.com', [email], fail_silently=False)
    
# creating a function to reject application and automatically send an email to the applicant. also delete the application from the database

    # def reject_application(self, request, queryset):
    #     queryset.update(status='Rejected')
    # reject_application.short_description = "Reject Application"
    # # send an email to the applicant
    def reject_application(self, request, queryset):
#        queryset.update(status='Rejected')
        # getting the email of the applicant
        email = queryset.values('email')
        # getting name of the applicant
        full_name = queryset.values('full_name')
        send_mail(
            'Application Rejected',
            f"Dear {full_name}, \nPlease we are sorry to inform you that your application has been rejected. \nThank you for applying to Halleluya properties limited. \nWe wish you the best in your future endeavors.", 'info@halleluyapropertieslimited.com',
            [email], fail_silently=False)
        # deleting the application from the database
        queryset.delete()


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