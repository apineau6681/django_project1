from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Profile
from django.http import HttpResponseRedirect
from . import forms

# Create your views here.


def index(request):
    context_dict = {'text': 'hello world', 'number': 100}
    return render(request, 'first_app/index.html', context_dict)


def other_page(request):
    return render(request, 'first_app/other.html')


def relative(request):
    return render(request, 'first_app/relative_url_templates.html')


def form_profile(request):
    form = forms.FormProfile

    if request.method == 'POST':
        form = forms.FormProfile(request.POST)

        if form.is_valid():
            # DO SOMETHING CODE
            print("VALIDATION SUCCESS!")

            # saving the profile data
            profile = Profile()
            profile.first_name = form.cleaned_data['first_name']
            profile.last_name = form.cleaned_data['last_name']
            profile.birth_date = form.cleaned_data['birth_date']
            profile.country = form.cleaned_data['country']
            profile.address = form.cleaned_data['address']
            profile.email = form.cleaned_data['email']
            profile.save()
            # redirect to Home Page
            return HttpResponseRedirect('/')

        else:
            print("NO SUCCESS")

    return render(request, 'first_app/create_profile.html', {'form': form})


def profiles(request):
    profile_records = Profile.profiles.all()  # calling Manager object
    profile_dict = {'profile_records': profile_records}
    return render(request, 'first_app/profiles.html', context=profile_dict)


def index2(request):
    # return HttpResponse("<em>Salut les FDP!</em>")
    my_dict = {'insert_me': "Salut les FDP!"}
    return render(request, 'first_app/index2.html', context=my_dict)


def view(request):
    return HttpResponse("<em>VIEW?</em>")


def homepage(request):
    return HttpResponse("<em>Home Page</em>")
