from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('',views.main,name='main'),
    path('ctasks/', views.ctasks, name='ctasks'),
    path('cnotification/', views.cnotification, name='cnotification'),
    path('creport/', views.creport, name='creport'),
    path('cdashboard/',views.cdashboard,name='cdashboard'),
    path('clogin/',views.clogin,name='clogin'),
    path('Mlogin/dashboard.html/',views.dashboard,name='dashboard'),
    path('login/',views.login,name='login'),
    path('Mlogin/',views.Mlogin,name='Mlogin'),
    path('Mproject/',views.Mproject,name='Mproject'),
    path('notification/',views.notification,name='notification'),
    path('report/',views.report,name='report'),
    path('signup/',views.signup,name='signup'),
    path('tasks/',views.tasks,name='tasks'),
    path('tdashboard/',views.tdashboard,name='tdashboard'),
    path('tgroups/',views.tgroups,name='tgroups'),
    path('tlogin/',views.tlogin,name='tlogin'),
    path('tnotification/',views.tnotification,name='tnotification'),
    path('tproject/',views.tproject,name='tproject'),
    path('treport/',views.treport,name='treport'),
    path('tsignup/',views.tsignup,name='tsignup'),
    path('ttasks/',views.ttasks,name='ttasks'),
]

urlpatterns+=staticfiles_urlpatterns()