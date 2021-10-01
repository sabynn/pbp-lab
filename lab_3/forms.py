from lab_1.models import Friend
from django import forms

# from https://stackoverflow.com/questions/3367091/whats-the-cleanest-simplest-to-get-running-datepicker-in-django
class DateInput(forms.DateInput):
    input_type = 'date'


class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = '__all__'
        widgets = {
            'dob': DateInput(),
        }
