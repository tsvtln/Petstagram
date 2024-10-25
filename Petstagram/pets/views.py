from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from Petstagram.common.forms import CommentForm
from Petstagram.pets.forms import PetAddForm, PetEditForm, PetDeleteForm
from Petstagram.pets.models import Pet


class PetAddPage(CreateView):
    model = Pet
    form_class = PetAddForm
    template_name = 'pets/pet-add-page.html'
    success_url = reverse_lazy('profile-details', kwargs={'pk': 1})

# def pet_add_page(request):
#     form = PetAddForm(request.POST or None)
#
#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#             return redirect('profile-details', pk=1)
#
#     context = {
#         'form': form,
#     }
#
#     return render(request, 'pets/pet-add-page.html', context)


def pet_delete_page(request, username: str, pet_slug: str):
    pet = Pet.objects.get(slug=pet_slug)
    form = PetDeleteForm(instance=pet)

    if request.method == 'POST':
        pet.delete()
        return redirect('profile-details', pk=1)

    context = {
        'form': form,
        'pet': pet,
    }

    return render(request, 'pets/pet-delete-page.html', context)


def pet_edit_page(request, username: str, pet_slug: str):
    pet = Pet.objects.get(slug=pet_slug)
    form = PetEditForm(request.POST or None, instance=pet)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('pet-details', username, pet_slug)
    else:
        context = {
            'form': form,
            'pet': pet,
        }

    return render(request, 'pets/pet-edit-page.html', context)


class PetDetailsPage(DetailView):
    model = Pet
    template_name = 'pets/pet-details-page.html'
    slug_url_kwarg = 'pet_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_photos'] = context['pet'].photo_set.all()
        context['comment_form'] = CommentForm()
        return context


# def pet_details_page(request, username: str, pet_slug: str):
#     pet = Pet.objects.get(slug=pet_slug)
#     all_photos = pet.photo_set.all()
#     comment_form = CommentForm()
#
#     context = {
#         'pet': pet,
#         'all_photos': all_photos,
#         'comment_form': comment_form,
#     }
#
#     return render(request, 'pets/pet-details-page.html', context)
