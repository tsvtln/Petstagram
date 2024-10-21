from django.shortcuts import render

from Petstagram.photos.models import Photo


def photo_add_page(request):
    return render(request, 'photos/photo-add-page.html')


def photo_edit_page(request, pk: int):
    return render(request, 'photos/photo-edit-page.html')


def photo_details_page(request, pk: int):
    photo = Photo.objects.get(pk=pk)
    likes = photo.like_set.all()
    comments = photo.comment_set.all()

    context = {
        'photo': photo,
        'likes': likes,
        'comments': comments
    }

    return render(request, 'photos/photo-details-page.html', context)
