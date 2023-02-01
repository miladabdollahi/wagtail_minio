from django.db import models
from django.utils.translation import gettext_lazy as _

from modelcluster.fields import ParentalKey
from wagtail.admin.panels import (FieldPanel, InlinePanel)
from wagtail.contrib.forms.models import AbstractFormField, AbstractForm, AbstractFormSubmission
from wagtail.fields import RichTextField

import apps.form.services as form_services


class FormField(AbstractFormField):
    page = ParentalKey('FormPage', on_delete=models.CASCADE, related_name='form_fields')

    panels = AbstractFormField.panels + [
        FieldPanel("clean_name"),
    ]

    def get_field_clean_name(self):
        return self.clean_name


class FormPage(AbstractForm):
    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)
    banner = models.ImageField(null=True, blank=True, upload_to='images')

    content_panels = AbstractForm.content_panels + [
        FieldPanel('intro'),
        FieldPanel('banner'),
        InlinePanel('form_fields', label="Form fields"),
        FieldPanel('thank_you_text'),
    ]
    
    def get_data_fields(self):
        data_fields = super().get_data_fields()
        
        data_fields += [
            ("otp_code", _("Otp code")),
        ]

        return data_fields
    
    def get_submission_class(self):
        """
        Returns submission class.

        You can override this method to provide custom submission class.
        Your class must be inherited from AbstractFormSubmission.
        """

        return FormCustomSubmission

    def process_form_submission(self, form):
        """
        Accepts form instance with submitted data, user and page.
        Creates submission instance.

        You can override this method if you want to have custom creation logic.
        For example, if you want to save reference to a user.
        """

        form_submission_queryset = self.get_submission_class().objects.filter(
            form_data__mobile=form.cleaned_data.get('mobile')
        )

        if form_submission_queryset.exists():
            return form_submission_queryset.first()

        mobile = form.cleaned_data.get('mobile')
        form.cleaned_data.update(otp_code=form_services.create_otp(mobile))

        return super().process_form_submission(form)


class FormCustomSubmission(AbstractFormSubmission):
    """
    form submission.
    """
