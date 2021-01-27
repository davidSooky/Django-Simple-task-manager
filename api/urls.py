from rest_framework import routers
from .viewsets import TaskViewSet
# from .viewsets import taskView
# from django.urls import path

router = routers.DefaultRouter()
router.register("task", TaskViewSet, "task")

urlpatterns = router.urls
# urlpatterns = [
#     path("task-list", taskView, name="task-list")
# ]