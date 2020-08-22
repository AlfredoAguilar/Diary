from django.utils.translation import ngettext
from django.utils.translation import gettext as _
from django.views.generic import TemplateView
from datetime import datetime


class ExamplesTranslations(TemplateView):
    template_name = "ex_i18n.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        # Case 1 => String (Message ID) translatable in context
        context['string_context'] = _('Hola')

        # Case 2 => Pluralization, when plural is irregular
        count_objects = 5
        str_i18n = ngettext(
            'valor de %(count_objects)d dolar',
            'valor de %(count_objects)d dolares',
            count_objects
        ) % {'count_objects': count_objects}

        context['pluralization_string'] = str_i18n

        # Case 3 => Date Format, se puede formatear en el settings
        context['i18n_date'] = datetime.now()

        # Case 4 =>
        sentence = 'Bienvenido a mi sitio'
        context['computed_string'] = _(sentence)

        return context
