from django.contrib import admin

from .models import (
    Employer,
    CandidateProfile,
    Job,
    Application
)

admin.site.register(Employer)
admin.site.register(CandidateProfile)
admin.site.register(Job)
admin.site.register(Application)