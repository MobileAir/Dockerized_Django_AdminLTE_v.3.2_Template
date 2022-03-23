from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from .forms import ImageFileUploadForm, ChangePassForm, ProfileForm, WebSiteForm
from .models import Profile


def user_site(request, user):
    if request.method == 'POST':
        user = request.POST.get("user")
        web_url = request.POST.get("web_url")
        profile = get_object_or_404(Profile, user=request.user)
        print(user, web_url)
        profile.website = web_url
        profile.save()
        return JsonResponse({'error': False, 'message': 'Uploaded Successfully', 'website': web_url})


def image_upload_ajax(request, user):
    profile = request.user.profile
    if request.method == 'POST':
        form = ImageFileUploadForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return JsonResponse({'error': False, 'message': 'Uploaded Successfully'})
        else:
            return JsonResponse({'error': True, 'errors': form.errors})


class ProfileView(View):
    template_name = 'app/profile.html'
    context_object_name = 'profile'

    def get(self, request, user=None, *args, **kwargs):

        profile = get_object_or_404(User, username=user)
        upload_image_form = ImageFileUploadForm()
        change_password = ChangePassForm()
        profile_form = ProfileForm(instance=profile)
        # print(dir(profile_form.data.dict()))

        web_site_form = WebSiteForm()
        return render(request, 'account/profile.html', {'user_profile': profile,
                                                        'upload_image_form': upload_image_form,
                                                        'change_password': change_password,
                                                        'profile_form': profile_form,
                                                        'web_site_form': web_site_form,
                                                        })

    def post(self, request, user=None, *args, **kwargs):
        print(request)
        print('user', user)
        form = ProfileForm(request.POST)
        print('POST method', request.POST)

        if form.is_valid():
            profile_form = form.save()
            profile_form.save()
        return render(request, 'account/profile.html', {'profile_form': profile_form})


@login_required
def user_profile(request, user):
    profile = get_object_or_404(Profile, user=user)
    return render(request, 'app/profile.html', {'profile': profile})
