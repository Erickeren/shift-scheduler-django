from django import forms

class StaffForm(forms.Form):
    names = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'placeholder': 'Masukkan 4 nama, pisahkan dengan baris'}))
