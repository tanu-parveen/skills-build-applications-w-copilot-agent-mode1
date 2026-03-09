from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelTests(TestCase):
    def setUp(self):
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')
        tony = User.objects.create(name='Tony Stark', email='tony@marvel.com', team=marvel)
        clark = User.objects.create(name='Clark Kent', email='clark@dc.com', team=dc)
        workout = Workout.objects.create(name='Super Strength', description='Heavy lifting')
        Activity.objects.create(user=tony, workout=workout, duration=60)
        Leaderboard.objects.create(user=tony, score=100)

    def test_user_team(self):
        tony = User.objects.get(email='tony@marvel.com')
        self.assertEqual(tony.team.name, 'Marvel')

    def test_leaderboard_score(self):
        tony = User.objects.get(email='tony@marvel.com')
        lb = Leaderboard.objects.get(user=tony)
        self.assertEqual(lb.score, 100)
