from django.conf.urls import url
from basic_app import views

#tempalte URLs
#this --app_name-- is used when telling the project on the project/urls.py to skip the project URLS FILES
#instead use the app/URLS.py file.
#you would use the --app_name-- lis so
# template page html --- {% url 'basic_app:user_login'%}
#you can see the --:user_login-- is also called below.
app_name = "basic_app"

urlpatterns = [
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
]
