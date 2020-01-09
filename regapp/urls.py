from django.urls import path
from regapp import views
from django.views.generic import TemplateView
urlpatterns=[
    path('',TemplateView.as_view(template_name='index.html'),name='index'),
    path('login',TemplateView.as_view(template_name='login.html'),name='login'),
    path('signup',TemplateView.as_view(template_name='signup.html'),name='signup'),
    path('faculty',TemplateView.as_view(template_name='faculty.html'),name='faculty'),
    path('stureg',TemplateView.as_view(template_name='stureg.html'),name='stureg'),
    path('admins',TemplateView.as_view(template_name='admins.html'),name='admins'),
    path('student',TemplateView.as_view(template_name='student.html'),name='student'),
    path('atten',TemplateView.as_view(template_name='atten.html'),name='atten'),
    path('facreg',TemplateView.as_view(template_name='facreg.html'),name='facreg'),
    path('stuattv',TemplateView.as_view(template_name='stuattv.html'),name='stuattv'),
    path('fmarks',TemplateView.as_view(template_name='fmarks.html'),name='fmarks'),
    path('stleav',TemplateView.as_view(template_name='stleav.html'),name='stleav'),
    path('fleav',TemplateView.as_view(template_name='fleav.html'),name='fleav'),
    path('logins',views.ad,name='logins'),
    path('std',views.Stu,name='std'),
    #path('fac',views.Facu,name='fac'),
    path('stufetch',views.fetche,name='stufetch'),
    path('facfetch',views.fetf,name='facfetch'),
    path('submit',views.display,name='submit'),
    path('facdb',views.facdb,name='facdb'),
    #path('stu1',views.Sty,name='stu1'),
    path('sprof',views.stup,name='sprof'),
    path('fprof',views.facp,name='fprof'),
    path('fdrop',views.attendance,name='fdrop'),
    path('fattfetch',views.fetchatt,name='fattfetch'),
    path('stuattv2',views.stuat,name='stuattv'),
    path('fmarking',views.marks,name='fmarking'),
    path('fmafet',views.facmfe,name='fmafet'),
    path('stumarv',views.stuma,name='stumarv'),
    path('stuleav',views.sleave,name='stuleav'),
    path('stleafet',views.stlea_fet,name='stleafet'),
    path('flleev',views.fleave,name='flleev'),
    path('fleafet1',views.flea_fet,name='fleafet'),
    path('logouts',views.logoutt,name='logouts'),
    path('approvf',views.approvef,name='submit'),
    path('approvs',views.approves,name='submit1'),


    
]