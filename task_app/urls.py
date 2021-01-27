from django.urls import path
from task_app import views
from django.contrib.auth import views as auth_views

urlpatterns = [
#General urls
    path("", views.index, name="index"),
    path("register/", views.register_user, name="register"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
#Search field
    path("search_result/", views.user_search, name="search"),
#Search result (Engineer names)
    path("user_info/<str:username>", views.engineer_profile, name="user_info"),
#File exports
    path("export_csv/", views.export_csv, name="export_csv"),
    path("export_excel/", views.export_excel, name="export_excel"),
    path("export_pdf/", views.GeneratePDF.as_view(), name="export_pdf"),
    path("statistics/", views.StatisticsView.as_view(), name="statistics"),
#Profile
    path("profile/", views.user_profile, name="profile"),
    path("profile_update/", views.user_profile_update, name="profile_update"),
#Follow/Unfollow profile
    path("follow_profile/<str:username>", views.follow_profile, name="follow_user"),
    path("unfollow_profile/<str:username>", views.unfollow_profile, name="unfollow_user"),
#Holidays
    path("holidays/", views.user_holidays, name="holidays"),
    path("update_holidays/<str:pk>", views.update_holidays, name="update_holidays"),
    path("delete_holidays/<str:pk>", views.delete_holidays, name="delete_holidays"),
#Tasks
    path("create_task/", views.task_creation, name="create_task"),
    path("update_task/<str:pk>", views.update_task, name="update_task"),
    path("delete_task/<str:pk>", views.delete_task, name="delete_task"),
    path("task/<str:pk>/comments", views.task_comments, name="task_comments"),
    path("task/comments/delete/<str:pk>", views.delete_comment, name="delete_comment"),
    path("task/comments/update/<str:pk>", views.update_comment, name="update_comment"),
#Password reset views
    path("reset_password/", auth_views.PasswordResetView.as_view(), name="password_reset"),
    path("reset_password_sent/", auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path("reset/<uidb64>/<token>", auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("reset_password_complete/", auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]