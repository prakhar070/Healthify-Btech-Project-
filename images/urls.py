from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

	path('index/', views.IndexView.as_view(), name="index"),
	path('upload/', views.SaveImageView.as_view(), name="save"),
	path('centres/', views.CentresView.as_view(), name="centres"),

	#views for login and logout
	path('login/', auth_views.LoginView.as_view(), name="login" ),
	path('logout/', auth_views.LogoutView.as_view(), name="logout"),

	#views for changing password
	path('password_change/', auth_views.PasswordChangeView.as_view(), name="password_change"),
	path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name="password_change_done"),
	path('password_reset/', auth_views.PasswordResetView.as_view(), name="password_reset"),
	path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
	path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
	path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

	#views for registration
	path('register/', views.register, name= "register"),
	path('email/', views.email, name= "email"),

]
