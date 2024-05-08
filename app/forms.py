from django import forms
from django.core.exceptions import ValidationError
#
from .models import UserRegistration

class UserRegistrationForm(forms.ModelForm):
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'placeholder': 'Retype Password'}))

    class Meta:
        model = UserRegistration
        fields = ['first_name', 'last_name', 'email', 'category', 'password']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email Address'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")

        if password1 != password2:
            raise ValidationError("Passwords do not match.")

        return cleaned_data

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email Address'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


#
from .models import PageModel1

class PageForm1(forms.ModelForm):
    class Meta:
        model = PageModel1
        exclude= ['user']
        widgets = {
            'date_of_application': forms.DateInput(attrs={'type': 'date'}),
            'dob': forms.DateInput(attrs={'type': 'date'}),
            # Add more fields as needed
        }

#Page 2 form
from .models import PageModel2

class PageForm2(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PageForm2, self).__init__(*args, **kwargs)
        self.fields['college_class'].widget.attrs['readonly'] = True
        self.fields['college_class'].initial = "12th/HSC/Diploma"
        self.fields['school_class'].widget.attrs['readonly'] = True
        self.fields['school_class'].initial = "10th"

    class Meta:
        model = PageModel2
        exclude = ['user']  # Exclude user field since we handle it in the view
        widgets = {
            'phd_defence_date': forms.DateInput(attrs={'type': 'date'}),
            'phd_award_date': forms.DateInput(attrs={'type': 'date'}),
            'pg_completion_year': forms.DateInput(attrs={'type': 'date'}),
            'ug_completion_year': forms.DateInput(attrs={'type': 'date'}),
        }

#Page 3 form
from .models import PageModel3

class PageForm3(forms.ModelForm):
    class Meta:
        model = PageModel3
        exclude = ['user']
        widgets = {
            'joining_date': forms.DateInput(attrs={'type': 'date'}),
            'leaving_date': forms.DateInput(attrs={'type': 'date'}),
        }

#Page 4 form
from .models import PageModel4

class PageForm4(forms.ModelForm):
    class Meta:
        model = PageModel4
        fields = ['international_journal_papers', 'national_journal_papers', 'international_conference_papers',
                  'national_conference_papers', 'patents', 'books', 'book_chapters', 'google_scholar_link']
        
# Page 5 Form
from .models import PageModel5

class PageForm5(forms.ModelForm):
    class Meta:
        model = PageModel5
        exclude = ['user'] 

# Page 6 Form
from .models import PageModel6

class PageForm6(forms.ModelForm):
    class Meta:
        model = PageModel6
        exclude = ['user'] 


#Page 7 form
from .models import PageModel7

class PageForm7(forms.ModelForm):
    class Meta:
        model = PageModel7
        exclude = ['user']


#Page 8 form
from .models import PageModel8

class PageForm8(forms.ModelForm):
    class Meta:
        model = PageModel8
        exclude = ['user']

#page 9 form
from .models import PageModel9

class PageForm9(forms.ModelForm):
    class Meta:
        model = PageModel9
        fields = ['declaration_agreed']