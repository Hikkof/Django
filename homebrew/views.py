from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.apps import apps
from django.shortcuts import render, get_object_or_404, redirect
from .forms import NewWeaponForm, NewArmorForm, NewItemForm, NewCareerForm, NewHomebrewForm
from .models import Homebrew, Item, Weapon, Armor, Career


def browse(request):
    query = request.GET.get('query', '')
    category = request.GET.get('category', '')

    homebrews = Homebrew.objects.all()[::-1]
    if category == "Armors":
        homebrews = Armor.objects.all()[::-1]
    elif category == "Items":
        homebrews = Item.objects.all()[::-1]
    if category == "Weapons":
        homebrews = Weapon.objects.all()[::-1]
    if category == "Careers":
        homebrews = Career.objects.all()[::-1]

    if query:
        homebrews = homebrews.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, 'homebrew/browse.html',
    {
        'homebrews' : homebrews,
        'query' : query
    })


def detail(request, pk):
    try:
        homebrew = get_object_or_404(Armor, pk=pk)
    except:
        try:
            homebrew = get_object_or_404(Item, pk=pk)
        except:
            try:
                homebrew = get_object_or_404(Homebrew, pk=pk)
            except:
                pass

    try:
        homebrew = get_object_or_404(Weapon, pk=pk)
    except:
        pass

    try:
        homebrew = get_object_or_404(Career, pk=pk)
    except:
        pass

    # related_homebrews = Homebrew.objects.filter(category=homebrew.name).exclude(pk=pk)[0:3]

    return render(request, 'homebrew/detail.html',
        {
            'homebrew' : homebrew,
            # 'related_items' : related_items
        })


def select(request):
    homebrews = Homebrew.objects.all()[::-1]

    return render(request, 'homebrew/select.html', {'homebrews' : homebrews[0:3]})


@login_required
def new_weapon(request):
    if request.method == 'POST':
        form = NewWeaponForm(request.POST, request.FILES)
        if form.is_valid():
            weapon = form.save(commit=False)
            weapon.created_by = request.user
            weapon.save()
            return redirect('homebrew:detail' , pk=weapon.id)
    else:
        form = NewWeaponForm()

    return render(request, 'homebrew/weapon_form.html',
                  {
                      'form': form,
                      'title': 'New weapon'
                  })


@login_required
def new_armor(request):
    if request.method == 'POST':
        form = NewArmorForm(request.POST, request.FILES)
        if form.is_valid():
            armor = form.save(commit=False)
            armor.created_by = request.user
            armor.save()
            return redirect('homebrew:detail', pk=armor.id)
    else:
        form = NewArmorForm()

    return render(request, 'homebrew/armor_form.html',
                  {
                      'form': form,
                      'title': 'New armor'
                  })


@login_required
def new_item(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect('homebrew:detail', pk=item.id)
    else:
        form = NewItemForm()

    return render(request, 'homebrew/item_form.html',
                  {
                      'form': form,
                      'title': 'New Item'
                  })


@login_required
def new_career(request):
    if request.method == 'POST':
        form = NewCareerForm(request.POST, request.FILES)
        if form.is_valid():
            career = form.save(commit=False)
            career.created_by = request.user
            career.save()
            return redirect('homebrew:detail', pk=career.id)
    else:
        form = NewCareerForm()

    return render(request, 'homebrew/career_form.html',
                  {
                      'form': form,
                      'title': 'New Career'
                  })


@login_required
def new_homebrew(request):
    if request.method == 'POST':
        form = NewHomebrewForm(request.POST, request.FILES)
        if form.is_valid():
            homebrew = homebrew_form.save(commit=False)
            homebrew.created_by = request.user
            homebrew.save()
            return redirect('homebrew:detail', pk=homebrew.id)
    else:
        form = NewHomebrewForm()

    return render(request, 'homebrew/homebrew_form.html',
                  {
                      'form': form,
                      'title': 'New Homebrew'
                  })


@ login_required
def delete(request, pk):
    homebrew = get_object_or_404(Homebrew, created_by=request.user, pk=pk)
    homebrew.delete()

    return redirect('core:front')  # 'dashboard:index'


def edit(request, pk):
    try:
        homebrew = get_object_or_404(Armor, created_by=request.user, pk=pk)
        form = NewArmorForm(request.POST, request.FILES, instance=homebrew)
        class_type = 'armor'
    except:
        try:
            homebrew = get_object_or_404(Item, created_by=request.user, pk=pk)
            form = NewItemForm(request.POST, request.FILES, instance=homebrew)
            class_type = 'item'
        except:
            try:
                homebrew = get_object_or_404(Homebrew, created_by=request.user, pk=pk)
                form = NewHomebrewForm(request.POST, request.FILES, instance=homebrew)
                class_type = 'homebrew'
            except:
                pass

    try:
        homebrew = get_object_or_404(Weapon, created_by=request.user, pk=pk)
        form = NewWeaponForm(request.POST, request.FILES, instance=homebrew)
        class_type = 'weapon'
    except:
        pass

    try:
        homebrew = get_object_or_404(Career, created_by=request.user, pk=pk)
        form = NewCareerForm(request.POST, request.FILES, instance=homebrew)
        class_type = 'career'
    except:
        pass

    if request.method == 'POST':
        if form.is_valid():
            homebrew.save()
            form = type(form)(instance=homebrew)
            return redirect('homebrew:detail', pk=homebrew.id)
    else:
        form = type(form)(instance=homebrew)

    return render(request, f'homebrew/{class_type}_form.html',
        {
            'form' : form,
            'title' : f'Edit {class_type}'
        })


def edit_weapon(request, pk):
    weapon = get_object_or_404(Homebrew, created_by=request.user, pk=pk)

    if request.method == 'POST':
        form = EditHForm(request.POST, request.FILES, instance=weapon)
        if form.is_valid():
            weapon.save()
            return redirect('homebrew:detail', pk=weapon.id)
    else:
        form = EditWeaponForm(instance=weapon)

    return render(request, 'homebrew/weapon_form.html',
        {
            'form' : form,
            'title' : 'Edit weapon'
        })
