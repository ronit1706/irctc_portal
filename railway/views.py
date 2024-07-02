from django.shortcuts import render, redirect
from .models import Train, Booking
from .forms import RegisterForm, LoginForm, AddTrainForm, BookSeatForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.db import transaction



def home(request):
    return render(request, 'homepage.html')
def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Replace 'dashboard' with your actual dashboard URL name
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')

def dashboard(request):
    return render(request, 'dashboard.html')
from django.shortcuts import render, redirect
from .forms import AddTrainForm

def add_train(request):
    if request.method == 'POST':
        form = AddTrainForm(request.POST)
        if form.is_valid():
            form.save()  # This will create and save a new Train object
            return redirect('dashboard')  # Replace 'dashboard' with your actual dashboard URL name

    else:
        form = AddTrainForm()

    return render(request, 'add_train.html', {'form': form})
from django.shortcuts import render
from .models import Train

def get_seat_availability(request):
    if request.method == 'POST':
        source = request.POST.get('source')
        destination = request.POST.get('destination')

        trains = Train.objects.filter(source=source, destination=destination)

        return render(request, 'seat_availability.html', {'trains': trains})
    else:
        return render(request, 'dashboard.html')


@login_required
@transaction.atomic
def book_seat(request):
    if request.method == 'POST':
        form = BookSeatForm(request.POST)
        if form.is_valid():
            train_id = form.cleaned_data['train_id']
            seats = form.cleaned_data['seats']

            try:
                train = Train.objects.get(id=train_id)
            except Train.DoesNotExist:
                return redirect('seat_availability')

            if train.available_seats >= seats > 0:
                train.available_seats -= seats
                train.save()

                booking = Booking.objects.create(
                    train=train,
                    user=request.user,  # Assign the logged-in user
                    seats_booked=seats
                )

                return redirect('booking_details')
            else:
                return redirect('get_seat_availability')

    else:
        form = BookSeatForm()

    return render(request, 'book_seat.html', {'form': form})


def booking_details(request):
    user = request.user
    bookings = Booking.objects.filter(user=user)
    return render(request, 'booking.html', {'user': user, 'bookings': bookings})

def logout_user(request):
    logout(request)
    return redirect('home')
