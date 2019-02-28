from django import forms
from .models import Day

# Dayモデルの内容から自動的に作成
class DayCreateForm(forms.ModelForm):

    class Meta:
        model = Day
        fields = '__all__'  # ('title', 'text, 'date)
