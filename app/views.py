# views.py

from banjo.urls import route_get, route_post
from .models import RockClimb
from settings import BASE_URL

@route_get(BASE_URL + 'all')
def all_moves(args):
    all_list = []

    for climb in RockClimb.objects.all():
        all_list.append(climb.json_response())

    return {'all excercises and stretches':all_list}


@route_post(BASE_URL + 'new', args={'name':str, 'category': str, 'instructions': str, 'extra': str})
def new_move(args):
    new_move = RockClimb(
        name = args['name'],
        category = args['category'],
        instructions = args['instructions'],
        extra = args['extra'],
        likes = 0,
        views = 0
    )

    new_move.save()

    return {'exercise/stretch': new_move.json_response()}

@route_get(BASE_URL + 'one', args={'id': int})
def one_move(args):

    if RockClimb.objects.filter(id=args['id']).exists():
        one_move = RockClimb.objects.get(id=args['id'])

        return {'exercise/stretch': one_move.json_response()}

    else:
        return {'error': 'no exercise/stretch exists'}

@route_get(BASE_URL + 'category', args={'category': str})
def category(args):
    if RockClimb.objects.filter(category=args['category']).exists():
        category = RockClimb.objects.append(category=args['category'])

        return {'category': category.json_response()}

    else:
        return {'error': 'nothing available'}

@route_post(BASE_URL + 'edit', args={'id': int, 'name': str, 'category': str, 'instructions': str, 'extra': str})
def edit(args):
    if RockClimb.objects.filter(id=args['id']).exists():
        edit = RockClimb.objects.get(id=args['id'])
        edit.edit(args['name'])

        return{'new exercise/stretch': edit.json_response()}

    else:
        return {'error': 'no exercise/stretch exists'}