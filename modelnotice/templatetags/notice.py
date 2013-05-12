"""
Template tags for Django
"""

from django import template
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.models import ContentType

register = template.Library()

@register.tag(name="ajax_add_notice")
def do_ajax_add_notice(parser, token):
    
    try:
        # split_contents() knows not to split quoted strings.
        tag_name, obj = token.split_contents()
        
    except ValueError:
        raise template.TemplateSyntaxError("%r tag requires 1 argument" % token.contents.split()[0])
    return AjaxNoticeNode(obj)


class AjaxNoticeNode(template.Node):
    
    def __init__(self, obj):
        self.obj = template.Variable(obj)
    
    def render(self, context):
        try:
            obj = self.obj.resolve(context)
        except template.VariableDoesNotExist:
            return ''
        
        ctype = ContentType.objects.get_for_model(obj)
        object_type = ctype.model
        object_id = obj.id

        title = _(u'Found error?')
        action = reverse('ajax_notice_add', args=[object_type, object_id])
        html = '<a href="" class="dot hide add_new" data-add-div="notice-create-%s-%s" data-action="%s">%s</a> \
            <div id="notice-create-%s-%s" class="create-container" style="display:none;"></div>' % \
            (object_type, object_id, action, title, object_type, object_id)

        return html
