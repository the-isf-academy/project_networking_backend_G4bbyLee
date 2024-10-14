# views.py

from banjo.urls import route_get, route_post
from .models import RockClimb
from settings import BASE_URL

@route_get(BASE_URL + 'all')
def all_fortunes(args):
    all_list = []

    for fortune in RockClimb.objects.all():
        all_list.append(.json_response())

    return {'fortunes':fortunes_list}