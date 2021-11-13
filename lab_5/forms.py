from lab_2.models import Note
from django import forms


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'

    error_messages = {
        'required': 'Please fill all fields'
    }

    input_attrs = {
        'type': 'text',
    }

    sender = forms.CharField(label="From", required=True, max_length=50, widget=forms.TextInput(attrs=input_attrs),
                             error_messages=error_messages)
    to = forms.CharField(label="To", required=True, max_length=50, widget=forms.TextInput(attrs=input_attrs),
                         error_messages=error_messages)
    title = forms.CharField(label="Title", required=True, widget=forms.TextInput(attrs=input_attrs),
                            error_messages=error_messages)
    message = forms.CharField(label="Message", required=True, widget=forms.Textarea(attrs=input_attrs),
                              error_messages=error_messages)
