from django.apps import AppConfig
from django.contrib.auth.signals import user_logged_out
from django.db.models.signals import post_save
from django.conf import settings

TRACK_CACHE_ON_POSTSAVE = getattr(settings, 'TRACK_CACHE_ON_POSTSAVE')

class TrackingConfig(AppConfig):

    name = 'tracking'
    verbose_name = 'django-tracking2'

    def ready(self):
        from tracking import handlers
        from tracking.models import Visitor
        user_logged_out.connect(handlers.track_ended_session)
        if TRACK_CACHE_ON_POSTSAVE:
            post_save.connect(handlers.post_save_cache, sender=Visitor)
