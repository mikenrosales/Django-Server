"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from Plan_It_Teknoy import views
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage
from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy




app_name = 'Plan_It_Teknoy'

urlpatterns = [

    # Start of user pages
    path('', views.home, name="Home"),
    # for login microsoft
    path('microsoft_authentication/', include('microsoft_authentication.urls')),
    path('index/', views.IndexView.as_view(), name="index_view"),
    
    path('logout/', views.microsoft_logout, name="Logout"),
    # end of addition
    # path('logout/', views.logout, name='logout'),
    path("About/", views.about, name="About"),
    path("Contact/", views.contactView.as_view(), name="contact_view"),
    path("SignIn/", views.SignInView.as_view(), name="signin_view"),
    path("StudentSignUp/", views.SignUpStudentView.as_view(), name="signupS_view"),
    path("TeacherSignUp/", views.SignUpTeacherView.as_view(), name="signupT_view"),
    # Select Role url
    path("SelectRole/", views.SelectRoleView.as_view(), name="select_view"),
    # Main Page url
    path("Calendar/", views.CalendarViewNew.as_view(), name="calendar_view"),
    # Dashboard url
    path("Dashboard/", views.DashboardView.as_view(), name="dashboard_view"),
    # Announcements url
    path("Announcements/", views.AnnouncementsView.as_view(), name="announcements_view"),
    path("DocumentGenerator/", views.DocGenView.as_view(), name="docgen_view"),

    # End of user pages

    # icon browser tab
    path("favicon.ico", RedirectView.as_view(
        url=staticfiles_storage.url("favicon.ico"))),

    path("All Events/", views.AllEventsListView.as_view(), name="all_events"),
    path(
        "Running Events/",
        views.RunningEventsListView.as_view(),
        name="running_events",
    ),
    path("Completed Events/", views.CompletedEventsListView.as_view(), name="completed_events"),

    
    # path("Notifications/", views.NotificationsListView.as_view(), name="notifications"),

    # student profile settings try
    path("student-profile/", views.SProfileSettings.as_view(), name="sprofile-settings_view"),
    # teacher profile settings try
    path("teacher-profile/", views.TProfileSettings.as_view(), name="tprofile-settings_view"),

    # Forgot Password url
    path("ForgotPassword/", views.ForgotPasswordView.as_view(), name="fp_view"),
    path("ForgotPassword/<code>/", views.ChangePasswordSentView.as_view(), name="fpt_view"),

    path('admin/', admin.site.urls),

    

    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

