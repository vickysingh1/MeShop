
from django.urls import path
from shop import views

urlpatterns = [
    path('', views.index,name="shophome"),
    path("about/",views.about,name="aboutus"),
    path("contact/",views.contact,name="contactus"),
    path("tracker/",views.tracker,name="tracking"),
    path("search/",views.search,name="search"),
    path("products/<int:myid>",views.productView,name="products"),
    path("checkout/",views.checkout,name="checkout"),
    path("login/",views.Login,name="Login"),
    
    



]