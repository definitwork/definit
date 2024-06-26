import json
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render
from main_app.functions import send_telegram_message
from main_app.models import (CompanyInfoAndContacts, CompanyDecisions,AboutCompany,
                             CompanyProjects, CompanyExpertise, CompanyAdvantages,
                             Employees)


def get_main_page(request):
    """ Главная страница """
    info_and_contacts = CompanyInfoAndContacts.objects.first()
    about_company = AboutCompany.objects.all()
    decisions = CompanyDecisions.objects.all()
    projects = CompanyProjects.objects.prefetch_related("projectresults_set")[:2]
    context = {
        "info_and_contacts": info_and_contacts,
        "about_company": about_company,
        "decisions": decisions,
        "projects": projects
    }
    return render(request, template_name='mainPage.html', context=context)


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
    about_company = AboutCompany.objects.all()
    projects = CompanyProjects.objects.prefetch_related("projectresults_set")

    paginator = Paginator(projects, 4)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "info_and_contacts": info_and_contacts,
        "about_company": about_company,
        "projects": projects,
        "page_obj": page_obj
    }
    return render(request, template_name='portfolio.html', context=context)


def get_team_page(request):
    """ Страница Команды """
    info_and_contacts = CompanyInfoAndContacts.objects.first()
    director = Employees.objects.get(job_title__icontains="директор компании")
    employees = Employees.objects.exclude(job_title__icontains="директор компании")
    context = {
        "info_and_contacts": info_and_contacts,
        "director": director,
        "employees": employees,
    }
    print(context)
    return render(request, template_name='team.html', context=context)


def get_blog_page(request):
    """ Страница Блог """
    info_and_contacts = CompanyInfoAndContacts.objects.first()
    context = {
        "info_and_contacts": info_and_contacts,
    }
    return render(request, template_name='blog.html', context=context)


def get_reels_page(request):
    """ Страница Reels """
    info_and_contacts = CompanyInfoAndContacts.objects.first()
    context = {
        "info_and_contacts": info_and_contacts,
    }
    return render(request, template_name='reels.html', context=context)


def get_contacts_page(request):
    """ Страница Контактов """
    info_and_contacts = CompanyInfoAndContacts.objects.first()
    context = {
        "info_and_contacts": info_and_contacts,
    }
    return render(request, template_name='contacts.html', context=context)


def callback(request):
    """ Отправляем данные в ТГ бота для обратной связи """
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name_user = data.get('name_user')
            phone_number_user = data.get('phone_number_user')

            if name_user == '' or phone_number_user == '':
                raise ValueError("Некорректные данные")

            # Отправка данных в бота Telegram
            bot_token = '7053287159:AAHmnyY9PQus0e1tID9s0zGDEbHjpP-MwGk'
            chat_id = '540697966'
            message = f'Имя: {name_user}\nТелефон: {phone_number_user}'
            send_telegram_message(bot_token, chat_id, message)

            return JsonResponse({'message': 'Данные успешно получены'})
        except json.JSONDecodeError:
            return JsonResponse({'message': 'Ошибка при декодировании JSON'}, status=400)
        except ValueError as e:
            return JsonResponse({'message': str(e)}, status=400)
    else:
        return JsonResponse({'message': 'Метод не разрешен'}, status=405)
