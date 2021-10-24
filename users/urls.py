from django.urls import path
from .views import Login,Register,AdvisorView,BookingView

urlpatterns = [
    path('login/',Login.as_view(),name='login'),
    path('register/',Register.as_view(),name='register'),
    path('<int:user_id>/advisor/',AdvisorView.as_view()),
    path('<int:user_id>/advisor/booking/',BookingView.as_view()),
    path('<int:user_id>/advisor/<int:advisor_id>/',BookingView.as_view()),

]