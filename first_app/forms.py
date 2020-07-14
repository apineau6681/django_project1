from django import forms
from django.core import validators
from django_countries.fields import CountryField
# from first_app.models import Profile


# Form example
class FormProfile(forms.Form):

    first_name = forms.CharField(widget=forms.TextInput)
    last_name = forms.CharField()
    birth_date = forms.DateField()
    country = CountryField().formfield()
    # gender = models.CharField(max_length=1)
    address = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()
    confirm_email = forms.EmailField(label="Confirm your email:")

    # botcatcher to catch malicious bot on the website
    # field in html in background
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)])

# validate form content

    def clean(self):
        # all cleanded data for the entire form
        all_clean_data = super().clean()
        email = all_clean_data['email']
        confirm_email = all_clean_data['confirm_email']

        if email != confirm_email:
            raise forms.ValidationError("Please make sure emails match")


"""
# ModelForm example

class FormProfile(forms.ModelForm):
    class Meta:
        model = Profile
        # fields name in form and model shall be the same
        # fields = ['first_name', 'last_name', 'birth_date', 'nationality', 'address', 'email']
        fields = '__all__'
"""
