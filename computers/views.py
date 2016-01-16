# Create your views here.
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from .models import Computer
from tas.models import Course, Request
from django.core.cache import cache

import logging

logger = logging.getLogger(__name__)


ROOMS_CACHE_KEY = "ROOMS_CACHE_KEY"
LABS_CACHE_KEY = "LABS_CACHE_KEY"


# Necessary so that the csrf token can be loaded for the ajax calls on the page.
@ensure_csrf_cookie
def ModularHomePage(request):
    template_params = {}

    room_nums = cache.get(ROOMS_CACHE_KEY)
    if not room_nums or room_nums:
        rooms = Computer.objects.distinct('room_number').order_by('room_number')
        room_nums = rooms.values_list('room_number', flat=True)
        cache.set(ROOMS_CACHE_KEY, room_nums)

    courses = Course.objects.all()
    open_requests = Request.objects.all()

    for course in courses:
        course.count = open_requests.filter(course=course).count()

    template_params['rooms'] = room_nums
    template_params['courses'] = courses

    return render(request, 'logged_in.html', template_params)
