from .serializers import TaskSerializer
from rest_framework import viewsets
from task_app.models import Task
# from rest_framework.response import Response
# from rest_framework.decorators import api_view


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# @api_view(["GET"])
# def taskView(request):
#     tasks =Task.objects.all()
#     serializer = TaskSerializer(tasks, many=True)

#     return Response(serializer.data)