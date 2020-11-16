from django.urls import path, include


app_name = "students"

urlpatterns = [
    # path("mypage/", include("app.site_student.mypage.urls"), name="mypage"),
    path("student-profile/", include("app.site_student.student_profile.urls"), name="student_profile"),
]
