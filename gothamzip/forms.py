import re
from django import forms
from django.core.exceptions import ValidationError


def zip_validator(value: str):
    if not value.isdigit():
        raise ValidationError("Gotham Zip codes are digits only.")
    if not 99999 < int(value) < 1000000:
        raise ValidationError("Valid Gotham Zip Codes are between 100,000 and 999,999.")
    match = re.search(r'(0.0|1.1|2.2|3.3|4.4|5.5|6.6|7.7|8.8|9.9)', value)
    if match:
        raise ValidationError(
            "Nice try, Joker. {} is not allowed.".format(match.group(1)),
        )


class ZipForm(forms.Form):
    zip = forms.CharField(
        label='',
        validators=[zip_validator],
        widget=forms.NumberInput(attrs={"placeholder": "ZIP CODE"}),
    )
