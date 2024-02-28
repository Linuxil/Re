from django.forms import ModelForm
from .models import Out_of_order
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

class Out_of_order_form(ModelForm):
    class Meta:
        model = Out_of_order
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'employee',
            'template',
            'message',
            'position',
            Submit('submit', 'Submit', css_class='btn-primary')
        )