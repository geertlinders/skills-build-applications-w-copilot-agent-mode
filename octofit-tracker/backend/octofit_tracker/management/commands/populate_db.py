
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models
from pymongo import MongoClient
from octofit_tracker import models as app_models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'


    def handle(self, *args, **options):
        # Verwijder bestaande data direct uit MongoDB-collecties met pymongo
        client = MongoClient('mongodb://localhost:27017/')
        db = client['octofit_db']
        for coll in ['user', 'team', 'activity', 'leaderboard', 'workout']:
            db[coll].delete_many({})

        # Teams
        marvel = app_models.Team.objects.create(name='Marvel')
        dc = app_models.Team.objects.create(name='DC')

        # Users
        ironman = app_models.User.objects.create(email='ironman@marvel.com', name='Iron Man', team=marvel)
        spiderman = app_models.User.objects.create(email='spiderman@marvel.com', name='Spider-Man', team=marvel)
        batman = app_models.User.objects.create(email='batman@dc.com', name='Batman', team=dc)
        superman = app_models.User.objects.create(email='superman@dc.com', name='Superman', team=dc)

        # Workouts
        w1 = app_models.Workout.objects.create(name='Pushups', description='Pushups workout')
        w2 = app_models.Workout.objects.create(name='Running', description='Running workout')

        # Activities
        app_models.Activity.objects.create(user=ironman, workout=w1, duration=30)
        app_models.Activity.objects.create(user=spiderman, workout=w2, duration=45)
        app_models.Activity.objects.create(user=batman, workout=w1, duration=20)
        app_models.Activity.objects.create(user=superman, workout=w2, duration=60)

        # Leaderboard
        app_models.Leaderboard.objects.create(user=ironman, score=100)
        app_models.Leaderboard.objects.create(user=spiderman, score=90)
        app_models.Leaderboard.objects.create(user=batman, score=95)
        app_models.Leaderboard.objects.create(user=superman, score=110)

        self.stdout.write(self.style.SUCCESS('octofit_db succesvol gevuld met testdata!'))
