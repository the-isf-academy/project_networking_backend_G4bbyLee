# views.py

from banjo.urls import route_get, route_post
from .models import Exercise
from settings import BASE_URL

@route_get(BASE_URL + 'all')
def all_moves(args):
    all_list = []

    for climb in Exercise.objects.all():
        all_list.append(climb.json_response())

    return {'all excercises and stretches':all_list}


@route_post(BASE_URL + 'new', args={'name':str, 'category': str, 'instructions': str, 'extra': str})
def new_move(args):
    new_move = Exercise(
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

    if Exercise.objects.filter(id=args['id']).exists():
        one_move = Exercise.objects.get(id=args['id'])
        one_move.increase_views()

        return {'exercise/stretch': one_move.json_response()}

    else:
        return {'error': 'no exercise/stretch exists'}


@route_get(BASE_URL + 'category', args={'category_filter': str})
def category(args):
    category_filter = []

    if Exercise.objects.filter(category__contains=args['category_filter']).exists():
        for climb in Exercise.objects.filter(category__contains=(args['category_filter'])):
            category_filter.append(climb.json_response())
        
        return {'category': category_filter}

    else:
        return {'error': 'no category exists'}


@route_post(BASE_URL + 'edit', args={'id': int, 'name': str, 'category': str, 'instructions': str, 'extra': str})
def change_information(args):
    if Exercise.objects.filter(id=args['id']).exists():
        one_move = Exercise.objects.get(id=args['id'])
        one_move.change_information(args['name'], args['category'], args['instructions'], args['extra'])

        return{'new exercise/stretch': one_move.json_response()}

    else:
        return {'error': 'no exercise/stretch exists'}


@route_post(BASE_URL + 'likes', args={'id': int})
def likes(args):
    if Exercise.objects.filter(id=args['id']).exists():
        likes = Exercise.objects.get(id=args['id'])
        likes.increase_likes()

        return {'likes': likes.json_response()}

    else:
        return {'error': 'no exercise/stretch exists'}


@route_get(BASE_URL + 'search', args={'keyword': str})
def search(args):
    keyword = []

    if Exercise.objects.filter(name__contains=args['keyword']).exists() or Exercise.objects.filter(category__contains=args['keyword']).exists() or Exercise.objects.filter(instructions__contains=args['keyword']).exists() or Exercise.objects.filter(extra__contains=args['keyword']).exists():
        for climb in Exercise.objects.filter(instructions__contains=(args['keyword'])):
            keyword.append(climb.json_response())
    
        return {'results': keyword}

    else:
        return {'error': 'there are no results'}