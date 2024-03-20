from django.core.paginator import Paginator
from django.shortcuts import render
from main_app.models import CompanyInfoAndContacts, CompanyDecisions, AboutCompany, CompanyProjects, CompanyExpertise, \
    CompanyAdvantages


def get_main_page(request):
    """ Главная страница """
    info_and_contacts = CompanyInfoAndContacts.objects.first()
    decisions = CompanyDecisions.objects.all()
    about_company = AboutCompany.objects.all()
    projects = CompanyProjects.objects.prefetch_related("projectresults_set")
    context = {
        "info_and_contacts": info_and_contacts,
        "decisions": decisions,
        "about_company": about_company,
        "projects": projects
    }
    return render(request, template_name='main.html', context=context)


def get_about_us_page(request):
    """ Страница О нас """
    info_and_contacts = CompanyInfoAndContacts.objects.first()
    about_company = AboutCompany.objects.all()
    expertise = CompanyExpertise.objects.all()
    advantages = CompanyAdvantages.objects.all()
    context = {
        "info_and_contacts": info_and_contacts,
        "about_company": about_company,
        "expertise": expertise,
        "advantages": advantages
    }
    return render(request, template_name='about_us.html', context=context)


def get_portfolio_page(request):
    """ Страница Портфолио + пагинатор """
    info_and_contacts = CompanyInfoAndContacts.objects.first()
    projects = CompanyProjects.objects.prefetch_related("projectresults_set")

    paginator = Paginator(projects, 4)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "info_and_contacts": info_and_contacts,
        "projects": projects,
        "page_obj": page_obj
    }
    return render(request, template_name='portfolio.html', context=context)