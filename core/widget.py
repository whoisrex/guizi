# from django.core.serializers import json
from django.forms import Textarea
from django.utils.safestring import mark_safe

try:
    import json
except ImportError:
    import django.utils.simplejson as json


class SimditorWidget(Textarea):
    class Media:
        css = {
            'all': ('/static/styles/simditor.css',)
        }
        js = ('/static/scripts/jquery.js', '/static/scripts/admin.js', '/static/scripts/module.min.js','/static/scripts/hotkeys.min.js',
              '/static/scripts/uploader.min.js', '/static/scripts/simditor.min.js',)

    def __init__(self, attrs=None, editor_options=None):
        super(SimditorWidget, self).__init__(attrs)
        self.editor_options = editor_options or {}

    def render(self, name, value, attrs=None):
        output = super(SimditorWidget, self).render(name, value, attrs)
        output += mark_safe(
            "<script type='text/javascript'> var editor = new Simditor({textarea: $('#%s'), upload: {url: '/uploads/', fileKey: 'Filedata',}});</script>"
            % (attrs['id']))
        return output
