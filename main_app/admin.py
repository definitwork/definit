from django.contrib import admin
from main_app.models import (CompanyInfoAndContacts, CompanyDecisions, AboutCompany,
                             CompanyProjects, Employees, ProjectResults,
                             CompanyExpertise, CompanyAdvantages)


@admin.register(CompanyInfoAndContacts)
class CompanyInfoAndContactsAdmin(admin.ModelAdmin):
    list_display = ("company_name",
                    "slogan",
                    "opening_hours",
                    "address",
                    "phone_number",
                    "email",
                    )


@admin.register(CompanyDecisions)
class CompanyDecisionsAdmin(admin.ModelAdmin):
    list_display = ("decision",)


@admin.register(AboutCompany)
class AboutCompanyAdmin(admin.ModelAdmin):
    list_display = ("info_block",)


@admin.register(CompanyProjects)
class CompanyProjectsAdmin(admin.ModelAdmin):
    list_display = ("project_name",
                    "description",
                    "image",
                    )


@admin.register(ProjectResults)
class ProjectResultsAdmin(admin.ModelAdmin):
    list_display = ("project",
                    "result",
                    )


@admin.register(CompanyExpertise)
class CompanyExpertiseAdmin(admin.ModelAdmin):
    list_display = ("stack",
                    "description",
                    )


@admin.register(CompanyAdvantages)
class CompanyAdvantagesAdmin(admin.ModelAdmin):
    list_display = ("advantage",)


@admin.register(Employees)
class EmployeesAdmin(admin.ModelAdmin):
    list_display = ("name", "job_title")
