from django.urls import path
from .views import get_main_page, get_about_us_page, get_portfolio_page, get_team_page, get_blog_page

urlpatterns = [
    path('', get_main_page, name="main"),
    path('about/', get_about_us_page, name="about"),
    path('portfolio/', get_portfolio_page, name="portfolio"),
    path('team/', get_team_page, name="team"),
    path('blog/', get_blog_page, name="blog"),
]