from django.template.loader import render_to_string

class NotificationBackend(object):
    slug = None
    display_name = None
    sensitivity = 2

    def path(self):
       return  "%s.%s" % (self.__module__, self.__class__.__name__)

    def should_send(self, notice):
        return notice.recipient.is_active and notice.get_setting(self).send

    def display_name(self):
        raise NotImplementedError

    def send(self, notice, messages, context, *args, **kwargs):
        raise NotImplementedError

    def render_message(self, template, notice_template, context, messages):
        return render_to_string(template,
                {'message': messages[notice_template],}, context)