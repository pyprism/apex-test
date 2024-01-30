from rest_framework import serializers
from pilotlog.models import PilotLog


class PilotLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = PilotLog
        fields = "__all__"
        read_only_fields = ["content"]
        write_only_fields = ["json_file"]
