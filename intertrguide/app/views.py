from django.contrib.auth import authenticate, login as login_user, logout as logout_user
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from .models import CustomUser,Category,Place,Description
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'index.html')

@login_required(login_url='login')
def aitg(request):
    return render(request, 'aitg.html')

def pricing(request):
    return render(request, 'pricing.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if not all([username, name, email, password, confirm_password]):
            messages.error(request, 'Please fill in all fields.')
            return redirect('signup')

        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, 'Email is already taken.')
            return redirect('signup')
        
        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, 'Username is already taken.')
            return redirect('signup')

        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return redirect('signup')

        user = CustomUser.objects.create_user(username=username, email=email, password=password, name=name)
        messages.success(request, "Your account has been created. You can now login.")
        

        # login_user(request, user)
        # return redirect('home')

    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not email or not password:
            messages.error(request, 'Please provide both email and password.')
            return redirect('login')

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login_user(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid email or password.')
            return redirect('login')
    
    return render(request, 'login.html')

def logout_view(request):
    logout_user(request)
    messages.success(request, "You have been logged out.")
    return redirect('login')

@login_required(login_url='login')
def settings(request):
    return render(request, 'settings_page.html')

def tr_in_blocks(request):
    categorys = Category.objects.all()
    places = Place.objects.all()
    return render(request, 'tr_in_blocks.html',
    {
     'categorys':categorys,
     'places':places,
     
     })
    
def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    places = Place.objects.filter(category=category)
    context = {
        'category': category,
        'places': places,
    }
    return render(request, 'category_detail.html', context)

def place_detail(request, pk):
    place = get_object_or_404(Place, pk=pk)
    descriptions = Description.objects.filter(place=place)
    
    context = {
        'place': place,
        'descriptions': descriptions,
    }
    return render(request, 'place_detail.html', context)

@login_required(login_url='login')
def delete_profile_picture(request):
    if request.method == 'POST':
        user = request.user  # Assuming you're using Django's built-in User model
        
        if user.image:  # Check if the image field is not empty
            user.image.delete()  # Delete the image file
            user.image = 'default.png'  # Set the image field to default.png
            user.save()
            messages.success(request, 'Profile picture deleted successfully.')
        else:
            messages.info(request, 'No profile picture to delete.')

        return redirect('settings')  # Redirect to the settings page or wherever you want

    # Handle GET requests or other cases
    return redirect('settings')

@login_required(login_url='login')
def change_profile_picture(request):
    if request.method == 'POST':
        user = request.user  # Assuming you're using Django's built-in User model
        new_image = request.FILES.get('new_image')  # Assuming the file input name is 'new_image'

        # Check if a new image was uploaded
        if new_image:
            # Delete the current image if it exists
            if user.image:
                user.image.delete()

            # Save the new image
            user.image = new_image
            user.save()
            messages.success(request, 'Profile picture updated successfully.')
        else:
            messages.error(request, 'No image selected.')

        return redirect('settings')  # Redirect to the settings page or wherever you want

    # Handle GET requests or other cases
    return redirect('settings')  # Redirect to the settings page if not a POST request
