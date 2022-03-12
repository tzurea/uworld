from django import forms

class SessionForm(forms.Form):
    maxQuestionCount = forms.IntegerField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Number of Questions",
                "class": "form-control"
            }
        ))
    timeLimit = forms.IntegerField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Time Limit",
                "class": "form-control"
            }
        ))
