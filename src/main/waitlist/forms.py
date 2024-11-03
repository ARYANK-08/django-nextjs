from django import forms


from .models import WaitlistEntry


class WaitlistEntryCreateForm(forms.ModelForm):
    # email = forms.EmailField()

    class Meta:
        model = WaitlistEntry
        fields = ['email']

    def clean_email(self):
        email = self.cleaned_data.get('email')

        return email