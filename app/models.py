# models.py

from banjo.models import Model, StringField, IntegerField, FloatField, BooleanField

class RockClimb(Model):
    name = StringField()
    category = StringField()
    instructions = StringField()
    extra = StringField()
    likes = IntegerField()
    views = IntegerField()

    def json_response(self):       
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'instructions': self.instructions,
            'extra': self.extra,
            'likes': self.likes,
            'views': self.views
        }

    def increase_likes(self):
        self.likes += 1
        self.save()

    def increase_views(self):
        self.views += 1
        self.save()

    def change_information(self, name, instructions, extra):
        self.name = name
        self.instructions = instructions
        self.extra = extra
        self.likes = 0
        self.save()

    


