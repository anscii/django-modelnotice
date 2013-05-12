from django import forms
from modelnotice.models import Notice
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.models import ContentType

class MyModelForm(forms.ModelForm):
    def as_div(self):
        return self._html_output(
            normal_row=u'<div class="js-active forms__width %(html_class_attr)s" >\
                                <div class="forms__i">\
                                    %(label)s %(field)s\
                                </div>\
                                %(help_text)s\
                                <div class="forms__hint">%(errors)s</div></div>',
            error_row=u'%s',
            row_ender=u'',
            help_text_html=u'<div class="forms__hint">%s</div>',
            errors_on_separate_row=False
        )
    forms.BaseForm.as_div = as_div

class NoticeForm(MyModelForm):
    class Meta:
        model = Notice
        fields = ('text','email')

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(NoticeForm, self).__init__(*args, **kwargs)
        if self.user.is_authenticated():
            del self.fields['email']
        

    def clean(self):
        super(NoticeForm, self).clean()
        cleaned_data = self.cleaned_data

        if not self.user.is_authenticated() and ('email' not in cleaned_data or not cleaned_data['email']):
            raise forms.ValidationError(_(u'Anonymous users must enter email to report notice.'))
        return cleaned_data
