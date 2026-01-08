from django import forms


class SearchForm(forms.Form):
    q = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search for tasks or users...", # Minor UI tweak
            }
        ),
    )
