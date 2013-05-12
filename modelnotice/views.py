from modelnotice.forms import NoticeForm

from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, Http404
from django.template import RequestContext

from exceptions import *
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.utils import simplejson
#from django.conf import settings
#from default_settings import RATINGS_VOTES_PER_IP

def ajax_notice_add(request, object_type, object_id, template="notice/ajax_add.html"):
    u"Ajax add notice for object"
    
    if request.is_ajax():
        try:
            ctype = ContentType.objects.get(model=object_type)
        except ObjectDoesNotExist:
            raise Http404
        
        action = reverse('ajax_notice_add',args=[object_type, object_id])

        if request.method == 'POST' and request.POST:
            form = NoticeForm(request.POST,user=request.user)

            if form.is_valid():
                notice = form.save(commit=False)
                notice.content_type = ctype
                notice.object_id = object_id
                if request.user.is_authenticated():
                    notice.user = request.user
                notice.save()
                result = {'response': unicode(_("Created")), 'result': 'success'}
            else:
                from django.template import loader
                t = loader.get_template(template)
                ctx = RequestContext(request, {'form': form, 'action':action})
                response = t.render(ctx)
                result = {'response': unicode(response), 'result': 'error'}
            return HttpResponse(simplejson.dumps(result), mimetype="application/json")
        else:
            form = NoticeForm(user=request.user)
            
            data = {'form':form, 'action':action}
            from django.views.generic.simple import direct_to_template
            
            return direct_to_template(request, template, extra_context=data)
    else:
        raise Http404
