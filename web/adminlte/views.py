from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions


class MixView(APIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    template_name = None

    def get(self, request):
        return render(request, self.template_name, {})


# def index(request):
#     return render(request, 'adminlte/index.html', {})
#
#
# def index2(request):
#     return render(request, 'adminlte/index2.html', {})
#
#
# def index3(request):
#     return render(request, 'adminlte/index3.html', {})
#
#
# def widgets(request):
#     return render(request, 'adminlte/pages/widgets.html', {})
#
