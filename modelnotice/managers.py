from django.db.models import Manager

from django.contrib.contenttypes.models import ContentType

class NoticeManager(Manager):
    def get_for_user_in_bulk(self, objects, user):
        objects = list(objects)
        if len(objects) > 0:
            ctype = ContentType.objects.get_for_model(objects[0])
            notices = list(self.filter(content_type__pk=ctype.id,
                                       object_id__in=[obj._get_pk_val() for obj in objects],
                                       user__pk=user.id))
            notice_dict = dict([(notice.object_id, notice) for notice in notices])
        else:
            notice_dict = {}
        return notice_dict
