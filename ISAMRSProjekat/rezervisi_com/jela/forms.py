from django import forms


from .models import Jelo


class JeloForm(forms.ModelForm):
    class Meta:
        model = Jelo
        fields = [
            "naziv",
            "opis",
            "image",
            "cena",
        ]