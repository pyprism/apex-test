from django.db import models


class PilotLogManager(models.Manager):
    def get_all(self):
        return self.order_by("created_at")

    def save_json(self, instance, file_content):
        instance.content = file_content.file.read().decode("utf-8")
        instance.save()
        return instance


class PilotLog(models.Model):
    json_file = models.FileField(upload_to="%Y/%m/%d/")
    content = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = PilotLogManager()

    def __str__(self):
        return self.json_file.name
