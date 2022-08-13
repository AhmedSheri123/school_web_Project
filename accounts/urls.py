from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("addUser",views.addUser, name="addUser"),
    path("qrGen/<int:id>", views.QrCodeShow, name="qrGen"),
    path("showUsers", views.showUsers, name="showUsers"),
    path('enterSchool', views.EnterSchool, name="enterSchool"),
    path('outSchool', views.outSchool, name="outSchool"),
    path("userViewer/<int:id>", views.UserViewer, name="userViewer"),
    path("getUserReport/<int:id>", views.getUserReport, name="getUserReport"),
    path("getAllUserReport", views.getAllUserReport, name="getAllUserReport"),
    path("backup", views.BackupData, name="backup"),
    path("importBackup", views.importBackup, name="importBackup"),
]