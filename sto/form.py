from django import forms
from .models import sto,iselect

class stoform(forms.ModelForm):
    class Meta:
        model = sto
        fields=('code',)


class selectform(forms.ModelForm):
    class Meta:
        model = iselect
        fields=('code','kmin','datanum')

class quantf(forms.Form):
    choic=(
        ('MACD','MACD'),
        ('KDJ','KDJ'),
        ('BOLL','BOLL'),
        ('RSI','RSI'),
    )
    code=forms.CharField(max_length=200,help_text='最大长度为200')
    choice=forms.ChoiceField(choices=choic,label='QUANT CHOICE')
    date=forms.IntegerField()
