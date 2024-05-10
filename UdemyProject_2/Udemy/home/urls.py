from django.urls import path
from . import views


urlpatterns = [

    path('', views.home, name='signin'),
    path('signin.html', views.signin_html, name='signin'),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('leave', views.leave, name='leave'),
    path('leaveform', views.leave_form, name='leaveform'),
    path('view_leaveform', views.view_leaveform, name='view_leaveform'),
    path('profile', views.view_profile, name='profile'),
    path('base', views.birthday, name='base'),
    path('goal', views.goal, name='goal'),
    path('feedback', views.feedback, name='feedback'),
    path('tree', views.tree, name='tree'),

]
