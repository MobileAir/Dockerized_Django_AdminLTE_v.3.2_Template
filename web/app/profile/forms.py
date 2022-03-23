from django import forms
from .models import Profile, ProfileManager
from allauth.account.forms import ChangePasswordForm


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('signature', 'gender', 'phone_number')
        exclude = ('user',)
        # widgets = {'author': forms.ChoiceField(choices=ProfileManager.GENDER_CHOICES)}

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['phone_number'].widget.attrs.update({
            'class': 'form-control',
            # 'value': '{{ user_profile.profile.phone_number }}',
        })
        self.fields['phone_number'].widget.attrs['placeholder'] = '(xxx)xxx-xxxx' or self.fields['phone_number'].label
        self.fields['gender'].widget.attrs.update({
            'class': 'form-control',
            # 'value': 'M',
        })
        self.fields['signature'].widget.attrs.update({
            'class': 'form-control',
            'rows': 2,
        })

    # def save(self, commit=True, *args, **kwargs):
    #     super(ProfileForm, self).__init__(*args, **kwargs)
    #     # print("Loop:")
        # for data, value in self.fields.items():
        #     print(dir(data), ":", dir(value))
        #     value.widget.attrs['placeholder'] = value.help_text


class ChangePassForm(ChangePasswordForm):
    def __init__(self, *args, **kwargs):
        super(ChangePassForm, self).__init__(*args, **kwargs)
        self.fields['oldpassword'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control'
        })


class ImageFileUploadForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image',)


class WebSiteForm(forms.Form):
    web_site = forms.URLField(label='',
                              widget=forms.TextInput(
                                  attrs={"placeholder": "Your site",
                                         "class": 'form-control url_field'},))

    class Meta:
        model = Profile
        fields = ('website')


class SignupForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'gender')

    def signup(self, request, user):
        # Save your user
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

        # user.profile.nationality = self.cleaned_data['nationality']
        user.profile.gender = self.cleaned_data['gender']
        user.profile.save()
