from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from .models import Engineer, Task, Holiday, Comment
from datetime import datetime, timedelta


# Taskform on the index page
class IndexTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["assigned_to", "start_date"]
        labels = {"assigned_to":"Create for:", "start_date": "Start date:"}
        widgets = {"start_date":forms.DateInput(attrs={"type":"date", "class":"form-input"})}

    def clean_start_date(self):
        #cleaned_data = super().clean()
        start_date = datetime.strptime(str(self.cleaned_data["start_date"]), "%Y-%m-%d").date()
        holidays = Holiday.objects.filter(owner=self.clean_assigned_to())

        for holiday in holidays:
            while holiday.start_date <= holiday.end_date:
                if start_date == holiday.start_date:
                    raise forms.ValidationError("Engineer will be out of office on this day.")
                holiday.start_date += timedelta(days=1)
        return start_date
    
    def clean_assigned_to(self):
        assigned_to = self.cleaned_data["assigned_to"]
        return assigned_to


# Taskform to create new tasks, inherits from IndexTaskForm
class TaskForm(IndexTaskForm):

    class Meta:
        model = Task
        fields = "__all__"
        widgets = {"start_date":forms.DateInput(attrs={"type":"date"}), "end_date":forms.DateInput(attrs={"type":"date"}),
                    "description":forms.Textarea(attrs={"rows":3})}
    

# Form to create new holidays for defined user
class HolidayForm(ModelForm):
    class Meta:
        model = Holiday
        fields = "__all__"
        labels = {"start_date": "Start date:", "end_date": "End date:"}
        widgets = {"start_date":forms.DateInput(attrs={"type":"date"}),
                    "end_date":forms.DateInput(attrs={"type":"date"})}

    def clean(self):
        cleaned_data = super().clean()
        start_date = datetime.strptime(str(cleaned_data["start_date"]), "%Y-%m-%d")
        end_date = datetime.strptime(str(cleaned_data["end_date"]), "%Y-%m-%d")

        if start_date > end_date:
            raise forms.ValidationError("Invalid input. Start date is bigger then end date.")
        return cleaned_data


# Form to register new user
class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(max_length=100, required=True)

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]

    def clean_email(self):
        # Get the email
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')

        if email and User.objects.filter(email=email).exclude(username=username).count():
            raise forms.ValidationError("This email address is already in use. Please select a different email address.")
        return email


# Form for user login
class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"name":"username", "type":"text"}))
    password = forms.CharField(widget=forms.TextInput(attrs={"name":"password", "type":"password"}))


# Form to show user profile
class UserProfileForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["readonly"] = True

    class Meta:
        model = Engineer
        fields = "__all__"
        exclude = ["owner", "profile_pic"]
        labels = {"phone_num":"Phone Number", "profile_pic":""}
        widgets = {"address":forms.Textarea(attrs={"rows":3, "style":"resize:none"})}


# Form to update user profile, inherits from UserProfileForm
class UserProfileFormActive(UserProfileForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if not field == "date_registered" and not field == "email":
                self.fields[field].widget.attrs["readonly"] = False
                
    class Meta(UserProfileForm.Meta):
        exclude = ["owner"]


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
        labels = {"content":"Comment:"}
        widgets = {"content":forms.Textarea(attrs={"rows":5, "style":"resize:none"})}