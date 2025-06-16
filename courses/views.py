from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from http import HTTPStatus
from .models import Course

# Create your views here.

def home(request):
    return render(request, 'courses/home.html')

class CourseView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return HttpResponse("Unauthorized", status=HTTPStatus.UNAUTHORIZED)
        courses = Course.objects.all()
        return render(request, 'courses/course_list.html', {'courses': courses})
