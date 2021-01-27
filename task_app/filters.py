import django_filters
from .models import Task
from django.forms import DateInput

#Filter for filtering tasks
class TaskFilter(django_filters.FilterSet):
    choices = ((True, "Completed"), (False, "Pending"))
    is_completed = django_filters.ChoiceFilter(choices=choices)
    start_date = django_filters.DateFilter(field_name="start_date", lookup_expr="gte", widget=DateInput(attrs={"type":"date", "class":"form-input"}), label="Start date:") 
    class Meta:
        model = Task
        fields = ["category", "is_completed", "start_date"]
