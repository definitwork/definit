from django.db import models


# Используется на Главной, Контакты и на всех остальных (берем название компании на О нас и номер телефона в хедере)
class CompanyInfoAndContacts(models.Model):
    company_name = models.CharField(max_length=255, verbose_name="Название компании")
    slogan = models.TextField(verbose_name="Девиз компании")
    opening_hours = models.CharField(max_length=50, verbose_name="Время работы")
    address = models.CharField(max_length=255, verbose_name="Адрес")
    phone_number = models.CharField(max_length=25, verbose_name="Телефон")
    email = models.EmailField(verbose_name="Электронная почта")

    class Meta:
        verbose_name = "Компания и контакты"
        verbose_name_plural = "Компания и контакты"

    def __str__(self):
        return self.company_name


# Используется на странице Главная
class CompanyDecisions(models.Model):
    decision = models.CharField(max_length=255, verbose_name="Предлагаемые нами решения")

    class Meta:
        verbose_name = "Наше решение"
        verbose_name_plural = "Наши решения"

    def __str__(self):
        return self.decision


# Используется на страницах Главная и О нас
class AboutCompany(models.Model):
    info_block = models.TextField(verbose_name="Инфоблок о компании")

    class Meta:
        verbose_name = "Инфоблок о компании"
        verbose_name_plural = "Инфоблок о компании"

    def __str__(self):
        return self.info_block


# Используется на страницах Главная и Портфолио
class CompanyProjects(models.Model):
    project_name = models.CharField(max_length=255, verbose_name="Название проекта")
    description = models.TextField(verbose_name="Описание проекта")
    image = models.ImageField(upload_to="./project_img", verbose_name="Обложка проекта")
    link = models.CharField(max_length=255, default="#", verbose_name="Ссылка на сайт")

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"

    def __str__(self):
        return self.project_name


# Используется на страницах Главная и Портфолио
class ProjectResults(models.Model):
    project = models.ForeignKey('CompanyProjects', on_delete=models.CASCADE, verbose_name="Проект")
    result = models.CharField(max_length=255, verbose_name="Результат по проекту")

    class Meta:
        verbose_name = "Результаты по проекту"
        verbose_name_plural = "Результаты по проекту"

    def __str__(self):
        return self.result


# Используется на странице О нас
class CompanyExpertise(models.Model):
    stack = models.CharField(max_length=255, verbose_name="Стек технологий")
    description = models.TextField(verbose_name="Описание стека")

    class Meta:
        verbose_name = "Стек технологий"
        verbose_name_plural = "Стек технологий"

    def __str__(self):
        return self.stack


# Используется на странице О нас
class CompanyAdvantages(models.Model):
    advantage = models.CharField(max_length=255, verbose_name="Преимущество")
    description = models.TextField(default="", verbose_name="Описание")

    class Meta:
        verbose_name = "Преимущество"
        verbose_name_plural = "Преимущества"

    def __str__(self):
        return self.advantage