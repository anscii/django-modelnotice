"""
Template tags for Django
"""

from django import template
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

register = template.Library()

@register.tag(name="ajax_add_notice")
def do_ajax_add_notice(parser, token):
    try:
        # split_contents() knows not to split quoted strings.
        tag_name, object_type, object_id = token.split_contents()
        
    except ValueError:
        raise template.TemplateSyntaxError("%r tag requires 2 arguments" % token.contents.split()[0])
    if not (object_type[0] == object_type[-1] and object_type[0] in ('"', "'")):
        raise template.TemplateSyntaxError("%r tag's first argument should be in quotes" % tag_name)
    return AjaxNoticeNode(object_type[1:-1], object_id)


class AjaxNoticeNode(template.Node):
    
    def __init__(self, object_type, object_id):
        self.object_type = object_type
        self.object_id = template.Variable(object_id)
    
    def render(self, context):
        try:
            object_id = self.object_id.resolve(context)
        except template.VariableDoesNotExist:
            return ''
        object_type = self.object_type
        title = _(u'Found error?')
        action = reverse('ajax_notice_add', args=[object_type, object_id])
        html = '<a href="" class="dot hide add_new" data-add-div="notice-create-%s-%s" data-action="%s">%s</a> \
            <div id="notice-create-%s-%s" class="create-container" style="display:none;"></div>' % \
            (object_type, object_id, action, title, object_type, object_id)

        return html
