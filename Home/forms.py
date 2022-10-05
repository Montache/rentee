from django import forms
from django.forms import ModelForm
from .models import Listing
from .models import Category

choices=Category.objects.all().values_list('Name','Name')
choice_list=[]
for item in choices:
    choice_list.append(item)

class ListingForm(ModelForm):
    class Meta:
        model=Listing
        fields=('Name','Category','Description','Location', 'ListingImage','Contact','HourlyRate', 'DailyRate', 'WeeklyRate', 'MonthlyRate')

        widgets={
            'Name':forms.TextInput(attrs={'class':'form-control'}),
            'Category':forms.Select(choices=choice_list, attrs={'class':'form-control'}),
            'Description':forms.Textarea(attrs={'class':'form-control'}),
            'Location':forms.TextInput(attrs={'class':'form-control'}),
            # 'ListingImage':forms.ImageField(attrs={'class':'form-control'}),
            'Contact':forms.TextInput(attrs={'class':'form-control'}),
            'HourlyRate':forms.TextInput(attrs={'class':'form-control'}),
            'DailyRate':forms.TextInput(attrs={'class':'form-control'}),
            'WeeklyRate':forms.TextInput(attrs={'class':'form-control'}),
            'MonthlyRate':forms.TextInput(attrs={'class':'form-control'}),
        }
