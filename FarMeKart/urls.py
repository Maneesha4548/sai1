from django.urls import path
from FarMeKart import views
from django.contrib.auth import views as ad

urlpatterns = [
    path('',views.home,name="hm"),
    path('lg/',ad.LoginView.as_view(template_name="html/login.html"),name="lgo"),
    path('reg/',views.registration,name="rg"),
    path('lgo/',ad.LogoutView.as_view(template_name='html/logout.html'),name="logo"),
    path('ch/',views.cgf,name="cg"),
    path('veg/',views.veg,name="veg"),
    path('pro/',views.profile,name="pf"),
    path('upr/',views.updprofile,name="upf"),
    path('ds/',views.dashboard,name="dsh"),
    path('dsf/',views.farmerdashboard,name="fdsh"),
    path('cn/',views.contact,name="ct"),
    path('ab/',views.about,name="au"),
    path('dt/',views.vegf,name="da"),
    path('infodelete/<int:et>',views.infodelete,name='infodelete'),
    path('ed/<int:y>/',views.itemupdate,name="ue"),
    path('items/',views.items,name="items"),
    path('ct/<int:id>/',views.addcart,name="ca"),
    path('us/',views.usr,name="cb"),
    path('reqp/',views.requestform,name='pm'),
    path('gper/',views.adminpermissions,name='gperm'),
    path('eper/<int:k>/',views.updatepermissions,name='up'),
    path('dele/<int:id>/',views.userdelete,name='delete'),
    path('addcart/<int:id>/',views.addcart,name="addcart"),
    path('cartdetails/',views.cartdetails,name="cartdetails"),

]