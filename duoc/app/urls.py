from django.urls import path
from . import views

urlpatterns = [
    path('', views.EstudianteList.as_view(), name='estudiante_lista'),
    path('view/<int:pk>', views.EstudianteDetail.as_view(), name='estudiante_detalle'),
    path('new', views.EstudianteCreate.as_view(), name='estudiante_nuevo'),
    path('edit/<int:pk>', views.EstudianteUpdate.as_view(), name='estudiante_editar'),
    path('delete/<int:pk>', views.EstudianteDelete.as_view(), name='estudiante_borrar'),
]
