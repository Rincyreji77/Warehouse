from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
    path('about/',views.about),
    path('contact/',views.contact),
    path('admin_login/',views.admin_login),
    path('admin_home/',views.admin_home),
    path('user_login/',views.user_login),
    path('user_home/',views.user_home),
    path('signup/',views.signup),
    path('add_product/',views.add_product),
    path('product_view/',views.product_view),
    path('user_view/',views.user_view),
    path('purchase/',views.purchase),
    path('order_list/',views.order_list),
    path('usord_view/',views.order_view),
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>',views.update),
    path('delete/<int:id>',views.destroy),


]