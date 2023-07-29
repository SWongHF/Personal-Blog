from django.apps import AppConfig


class PostConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'post'

    def ready(self):
        from . import signals
        #from .models import LastActivityRecord
        #if (not LastActivityRecord.objects.filter().exists()):
        #    x=LastActivityRecord.create()
        #    x.save()
