from django.urls import path
from . import views

urlpatterns = [
    path('', views.view, name="view"),
    path('<pk>', views.detail, name="detail"),
    path('create/project', views.create, name="creates"),
    path('create/task/<pk>', views.createtask, name="createtask"),
    path('update/<pk>', views.update, name="update"),
    path('updates/<pk>', views.updatetask, name="updatetask"),
    path('viewtask/<pk>', views.viewtask, name="viewtask"),
    path('create/subtask<pk>', views.createsubtask, name="createsubtask"),
    path('view/task/<pk>', views.viewsub, name="viewsub"),
    path('view/task/subtask/<pk>', views.updatesubtask, name="updatesubtask")
]