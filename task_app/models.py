from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from .managers import TaskCompletedManager, TaskNotCompletedManager

# Create your models here.

class Engineer(models.Model):
    owner = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    address = models.TextField(max_length=100, null=True, blank=True)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    phone_num = models.CharField(max_length=13, null=True, blank=True)
    email= models.EmailField(null=True)
    position = models.CharField(max_length=50, null=True, blank=True)
    date_registered = models.DateField(null=True, default=timezone.now)
    profile_pic = models.ImageField(default="images/profile.png", null=True, blank=True)

    def __str__(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return str(self.owner)


class Follower(models.Model):
    owner_id = models.ForeignKey(Engineer, null=True, related_name="follower_owner", blank=True, on_delete=models.CASCADE)
    follower_id = models.ForeignKey(Engineer, null=True, blank=True, related_name="following", on_delete=models.CASCADE)

    class Meta:
        unique_together = ["owner_id", "follower_id"]


class Following(models.Model):
    owner_id = models.ForeignKey(Engineer, null=True, related_name="following_owner", blank=True, on_delete=models.CASCADE)
    following_id = models.ForeignKey(Engineer, null=True, blank=True, related_name="follower", on_delete=models.CASCADE)

    class Meta:
        unique_together = ["owner_id", "following_id"]


class Task(models.Model):
    categories = (
        ("Balloon blowing", "Balloon blowing"),
        ("Swaging", "Swaging"),
        ("Proximal welding", "Proximal welding"),
        ("Pleating", "Pleating")
    )

    category = models.CharField(max_length=100, null=True, choices=categories, default=categories[0][0])
    description = models.TextField(null=True, blank=True)
    assigned_to = models.ForeignKey(Engineer, null=True, on_delete=models.CASCADE)
    start_date = models.DateField(null=True, default=timezone.now)
    end_date = models.DateField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)

    objects = models.Manager()
    completed_task = TaskCompletedManager()
    incompleted_task = TaskNotCompletedManager()

    class Meta:
        ordering = ["start_date"]

    def __str__(self):
        return self.category

    def get_absolute_url(self):
        return reverse("task_comments", kwargs={"pk":self.id})

class Holiday(models.Model):
    owner = models.ForeignKey(Engineer, on_delete=models.CASCADE)
    start_date = models.DateField(null=True, blank=False)
    end_date = models.DateField(null=True, blank=False)

    def __str__(self):
        return f"{self.start_date} : {self.end_date}"

class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    content = models.CharField(max_length=300, blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content[:30]

    class Meta:
        ordering = ["-update_date"]