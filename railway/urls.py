from django.urls import path
from .views import register_user,login_user,add_train,get_seat_availability,book_seat,booking_details, home, dashboard, logout_user


urlpatterns = [
    path('', home, name='home'),
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('add_train/', add_train, name='add_train'),
    path('get_seat_availability/', get_seat_availability, name='get_seat_availability'),
    path('book_seat/', book_seat, name='book_seat'),
    path('booking_details/', booking_details, name='booking_details'),
    path('logout/', logout_user, name='logout')
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
