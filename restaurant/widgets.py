from django.template.loader import render_to_string
#import django.forms as forms
import floppyforms as forms

class SelectWithPop(forms.Select):
    def render(self, name, *args, **kwargs):
        html = super(SelectWithPop, self).render(name, *args, **kwargs)
        popupplus = render_to_string('floppyforms/popupplus.html', {'field': name})
        return html+popupplus

class MultipleSelectWithPop(forms.SelectMultiple):
    def render(self, name, *args, **kwargs):
        html = super(MultipleSelectWithPop, self).render(name, *args, **kwargs)
        popupplus = render_to_string('floppyforms/popupplus.html', {'field': name})
        return html+popupplus

class PhoneInput(forms.TextInput):
    template_name = 'floppyforms/phoneinput.html'
