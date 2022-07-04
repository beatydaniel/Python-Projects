from django.forms import ModelForm
from .models import Account, Information


class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = '__all__'

class InformationForm(ModelForm):
    class Meta:
        model = Information
        fields = '__all__'
