from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create Users
        tony = User.objects.create(name='Tony Stark', email='tony@marvel.com', team=marvel)
        steve = User.objects.create(name='Steve Rogers', email='steve@marvel.com', team=marvel)
        bruce = User.objects.create(name='Bruce Wayne', email='bruce@dc.com', team=dc)
        clark = User.objects.create(name='Clark Kent', email='clark@dc.com', team=dc)

        # Create Workouts
        w1 = Workout.objects.create(name='Super Strength', description='Heavy lifting')
        w2 = Workout.objects.create(name='Flight', description='Aerobic flying')

        # Create Activities
        Activity.objects.create(user=tony, workout=w1, duration=60)
        Activity.objects.create(user=steve, workout=w2, duration=45)
        Activity.objects.create(user=bruce, workout=w1, duration=30)
        Activity.objects.create(user=clark, workout=w2, duration=50)

        # Create Leaderboard
        Leaderboard.objects.create(user=tony, score=100)
        Leaderboard.objects.create(user=steve, score=90)
        Leaderboard.objects.create(user=bruce, score=80)
        Leaderboard.objects.create(user=clark, score=95)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
