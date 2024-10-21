from django.shortcuts import render, redirect

from Petstagram.common.models import Like
from Petstagram.photos.models import Photo


def home_page(request):
    all_photos = Photo.objects.all()
    context = {
        'all_photos': all_photos
    }
    return render(request, 'common/home-page.html', context)


def likes_functionality(request, photo_id: int):
    liked_object = Like.objects.filter(to_photo_id=photo_id).first()
    if liked_object:
        liked_object.delete()
    else:
        like = Like(to_photo_id=photo_id)
        like.save()

    return redirect(request.META.get('HTTP_REFERER') + f'#{photo_id}')


# def share_functionality()