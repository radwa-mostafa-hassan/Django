from django.urls import path
from .views import show_todo, delete_task, show_task, mark_as_done, edit_task, add_task, update_task
app_name = 'todo'


urlpatterns = [
    path('home/', show_todo, name='home'),
    path('delete/<int:task_id>', delete_task, name='delete'),
    path('done/<int:task_id>', mark_as_done, name='done'),
    path('edit/<int:task_id>', edit_task, name='edit'),
    path('view/<int:task_id>', show_task, name='view'),
    path('home/add/', add_task, name='add'),
    path('home/update/<int:task_id>', update_task, name='update'),
]
