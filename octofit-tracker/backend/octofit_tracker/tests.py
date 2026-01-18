from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelSmokeTest(TestCase):
    def test_team_create(self):
        team = Team.objects.create(name='TestTeam')
        self.assertEqual(str(team), 'TestTeam')

    def test_user_create(self):
        team = Team.objects.create(name='TestTeam')
        user = User.objects.create(email='test@example.com', name='Test User', team=team)
        self.assertEqual(str(user), 'Test User')

    def test_workout_create(self):
        workout = Workout.objects.create(name='TestWorkout', description='desc')
        self.assertEqual(str(workout), 'TestWorkout')

    def test_activity_create(self):
        team = Team.objects.create(name='TestTeam')
        user = User.objects.create(email='test@example.com', name='Test User', team=team)
        workout = Workout.objects.create(name='TestWorkout', description='desc')
        activity = Activity.objects.create(user=user, workout=workout, duration=10)
        self.assertIn('Test User', str(activity))

    def test_leaderboard_create(self):
        team = Team.objects.create(name='TestTeam')
        user = User.objects.create(email='test@example.com', name='Test User', team=team)
        lb = Leaderboard.objects.create(user=user, score=42)
        self.assertIn('Test User', str(lb))
