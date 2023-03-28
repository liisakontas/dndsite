from django import forms

class d100Form(forms.Form):
    min_value = forms.IntegerField()
    max_value = forms.IntegerField()

    def clean(self):
        if self.cleaned_data.get("min_value") <= 0 or self.cleaned_data.get("min_value") >100:
            self.add_error("min_value", forms.ValidationError("Please select a value between 0 and 100.") )
        if self.cleaned_data.get("max_value") <= 0 or self.cleaned_data.get("max_value") >100:
            self.add_error("max_value", forms.ValidationError("Please select a value between 0 and 100.") )
        return self.cleaned_data