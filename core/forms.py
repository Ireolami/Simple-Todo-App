from django import forms
# from .models import UserTodo
class UserForm(forms.Form):
    text = forms.CharField(max_length=50,
            widget=forms.TextInput(attrs={'class': "form-control", 'placeholder':"Enter todo e.g. Delete junk files",
            'aria-label': "Todo",'aria-describedby':'add-btn'}))

    