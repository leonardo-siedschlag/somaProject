from django.urls import path
from . import  views

urlpatterns = [
 
    
    path('', views.lista_produtos, name='lista_produtos'),
    path('produtoNovo/', views.create_produto, name='create_produto'),
    path('update/<int:id>/', views.update_produto, name='update_produto'),
    path('delete/<int:id>/',views.delete_produto, name='delete_produto'),
    path('updateProdutoPage',views.updateProdutoPage, name='updateProdutoPage'),
    path('marcaNova/', views.create_marca, name='create_marca'),
    path('usuarioNovo/', views.create_usuario, name='create_usuario'),
    path('updateUserPage',views.updateUserPage, name='updateUserPage'),
    path('updateUser/<int:id>/', views.update_usuario, name='update_usuario'),
    path('dadosUser', views.dados_user, name='dados_user'),
    path('createCategory', views.create_categoria, name='create_categoria'),
    path('deleteUser/<int:id>/',views.delete_user, name='delete_user'),
    
]