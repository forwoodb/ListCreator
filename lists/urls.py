from django.urls import path, include
from .views import *

urlpatterns = [ 
    path('', index, name='index'),
    path('add_list/', add_list),
    path('del_list/<int:n>/', del_list),
    path('edit_list/<int:n>/', edit_list),
    path('update_list/<int:n>/', update_list),
    # List URLs
    path('list_page/<int:n>/', list_page, name="list_page"),
    path('add_item/<int:n>/', add_item),
    path('list_page/<int:l>/del_item/<int:i>/', del_item),
    path('list_page/<int:l>/edit_item/<int:i>/', edit_item),
    path('list_page/<int:l>/update_item/<int:i>/', update_item),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', SignUpView.as_view(template_name='registration/signup.html'), name='signup'),
    path('demo_login/', demo_login, name='demo_login')
]
