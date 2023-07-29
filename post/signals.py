import pytz
import datetime
from .models import Post, LastActivityRecord, Image
from django.dispatch import receiver
from django.db.models.signals import pre_delete, pre_save, post_save
import os


@receiver(pre_save, sender=Post)
def post_update_related_data(sender, instance, **kwargs):
    try:
        obj = sender.objects.get(id=instance.id)
    except sender.DoesNotExist:
        instance.wordCount = len(instance.content)
        activityRecord = LastActivityRecord.objects.all()[0]
        activityRecord.last_activity = datetime.datetime.now()
        activityRecord.save()
        pass
    else:
        if not (obj.title == instance.title and obj.category == instance.category and obj.introduction == instance.introduction and obj.content == instance.content and obj.hidden == instance.hidden and obj.priority == instance.priority):  # Field has changed
            instance.wordCount = len(instance.content)
            instance.updatedDate = datetime.datetime.now(
                pytz.timezone('Asia/Macao'))
            activityRecord = LastActivityRecord.objects.all()[0]
            activityRecord.last_activity = datetime.datetime.now()
            activityRecord.save()


@receiver(pre_delete, sender=Image)
def img_delete_related_data(sender, instance, **kwargs):
    if instance.img:
        if os.path.isfile(instance.img.path):
            os.remove(instance.img.path)


@receiver(post_save, sender=Image)
def img_update_related_data(sender, instance, **kwargs):
    if (instance.filename != instance.img.url.split('/')[-1]):
        instance.filename = instance.img.url.split('/')[-1]
        instance.save()
