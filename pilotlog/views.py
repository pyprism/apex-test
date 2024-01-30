from django.http import HttpResponse
from rest_framework.decorators import action
from rest_framework.response import Response

from pilotlog.models import PilotLog
from rest_framework import viewsets, status

from pilotlog.serializers import PilotLogSerializer
from pilotlog.utils.csv_gen import generate_csv


class PilotLogViewSet(viewsets.ModelViewSet):
    queryset = PilotLog.objects.get_all()
    serializer_class = PilotLogSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        file_uploaded = request.data.get("json_file")

        self.perform_create(serializer)
        PilotLog.objects.save_json(serializer.instance, file_uploaded)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=["GET"], name="Generate CSV")
    def generate_csv(self, request, pk=None):
        obj = self.get_object()
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="data.csv"'
        generate_csv(obj.content, response)
        return response
