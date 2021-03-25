from django.db import models
from django.db.models import JSONField  # type: ignore

from ..channel.models import Channel
from ..core.permissions import PluginsPermissions
from ..core.utils.json_serializer import CustomJsonEncoder


class PluginConfiguration(models.Model):
    identifier = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    channel = models.ForeignKey(
        Channel, blank=True, null=True, on_delete=models.SET_NULL
    )
    description = models.TextField(blank=True)
    active = models.BooleanField(default=False)
    configuration = JSONField(
        blank=True, null=True, default=dict, encoder=CustomJsonEncoder
    )

    class Meta:
        unique_together = ("identifier", "channel")
        permissions = ((PluginsPermissions.MANAGE_PLUGINS.codename, "Manage plugins"),)

    def __str__(self):
        return f"Configuration of {self.name}, active: {self.active}"
