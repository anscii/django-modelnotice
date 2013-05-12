from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from managers import NoticeManager

class Notice(models.Model):
    content_type = models.ForeignKey(ContentType, related_name="notices")
    object_id = models.PositiveIntegerField()
    text = models.TextField(_(u'notice'))
    user = models.ForeignKey(User, blank=True, null=True, related_name="notices")
    email = models.EmailField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True, editable=False)

    objects = NoticeManager()

    content_object = generic.GenericForeignKey()

    class Meta:
        verbose_name = _(u'notice')
        verbose_name_plural = _(u'notices')
        ordering = ['-date_added']

    def __unicode__(self):
        return u"%s left notice '%s' on %s" % (self.user_display, self.text, self.content_object)

    def user_display(self):
        if self.user:
            return "%s (id %s)" % (self.user.username, self.user.pk)
        return "Anonymous <%s>" % (self.email,)
    user_display = property(user_display)
