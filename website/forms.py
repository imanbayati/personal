from django.forms import ModelForm
from . models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields ='__all__'
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['site'].required = False
        self.fields['company'].required = False

