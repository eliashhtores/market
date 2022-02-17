from django import forms


class SalesSummaryForm(forms.Form):
    start_date = forms.DateField(
        required=True,
        widget=forms.DateInput(
            format='%Y-%m-%d',
            attrs={
                'class': 'form-control',
                'type': 'date'
            }
        )
    )

    end_date = forms.DateField(
        required=True,
        widget=forms.DateInput(
            format='%Y-%m-%d',
            attrs={
                'class': 'form-control',
                'type': 'date'
            }
        )
    )
