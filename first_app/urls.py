from django.urls import path
from first_app import views


# TEMPLATE TAGGING
app_name = 'first_app'

urlpatterns = [
    path('relative/', views.relative, name='relative'),
    path('other/', views.other_page, name='other'),
    path('relative_url_templates.html', views.relative, name='relative'),
    path('index2.html', views.index2, name='index2'),
    path('profiles.html', views.profiles, name='profiles'),
    path('create_profile.html', views.form_profile, name='create_profile'),
]
