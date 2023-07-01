from django.shortcuts import render, redirect

from djangoexam.web.models import Profile, Fruit

from .forms import ProfileCreateForm, FruitCreationForm, FruitEditForm, FruitDeleteForm, ProfileEditForm


def profile_existence_checker():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist:
        return None


def index(request):
    profile = profile_existence_checker()
    context = {
        'profile': profile
    }

    return render(request, 'index.html', context)


def dashboard(request):
    fruits = Fruit.objects.all()
    profile = profile_existence_checker()

    context = {
        'fruits': fruits,
        'profile': profile
    }
    return render(request, 'dashboard.html', context)


def create_fruit(request):
    profile = profile_existence_checker()
    if request.method == 'GET':
        form = FruitCreationForm()
    else:
        form = FruitCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'profile': profile,
        'form': form
    }

    return render(request, 'create-fruit.html', context)


def fruit_details(request, pk):
    profile = profile_existence_checker()
    fruit = Fruit.objects.filter(pk=pk).get()

    context = {
        'profile': profile,
        'fruit': fruit
    }
    return render(request, 'details-fruit.html', context)


def fruit_edit(request, pk):
    profile = profile_existence_checker()
    fruit = Fruit.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = FruitEditForm(instance=fruit)
    else:
        form = FruitEditForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'profile': profile,
        'form': form,
        'fruit': fruit

    }
    return render(request, 'edit-fruit.html', context)


def fruit_delete(request, pk):
    profile = profile_existence_checker()
    fruit = Fruit.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = FruitDeleteForm(instance=fruit)
    else:
        fruit.delete()
        return redirect('dashboard')

    context = {
        'profile': profile,
        'form': form,
        'fruit': fruit

    }
    return render(request, 'delete-fruit.html', context)


def create_profile(request):
    profile = profile_existence_checker()

    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'profile': profile,
        'form': form
    }

    return render(request, 'create-profile.html', context)


def profile_details(request):
    profile = profile_existence_checker()
    fruitscount = Fruit.objects.count()

    context = {
        'profile': profile,
        'fruitscount': fruitscount

    }
    return render(request, 'details-profile.html', context)


def profile_edit(request):
    profile = profile_existence_checker()
    if request.method == 'GET':
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_details')

    context = {
        'profile': profile,
        'form': form,

    }
    return render(request, 'edit-profile.html', context)


def profile_delete(request):
    profile = profile_existence_checker()
    fruits = Fruit.objects.all()
    if request.method == 'POST':
        if fruits:
            fruits.delete()
        profile.delete()
        return redirect('index')

    context = {
        'profile': profile
    }

    return render(request, 'delete-profile.html', context)
