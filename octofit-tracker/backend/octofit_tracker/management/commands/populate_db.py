from django.core.management.base import BaseCommand
from octofit_tracker.models import User
from django.db import connection
from djongo import models
from octofit_tracker.models import Team, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        print('Deleting existing data...')
        Activity.objects.filter(pk__isnull=False).delete()
        Workout.objects.filter(pk__isnull=False).delete()
        Leaderboard.objects.filter(pk__isnull=False).delete()
        Team.objects.filter(pk__isnull=False).delete()
            # UserProfile.objects.filter(pk__isnull=False).delete()  # Remove User references

        # Create teams

        marvel = Team.objects.create(name='Team Marvel')
        dc = Team.objects.create(name='Team DC')

        # Create users and assign to teams via UserProfile
        users = [
            User.objects.create(username='ironman', email='ironman@marvel.com', first_name='Tony', last_name='Stark'),
            User.objects.create(username='spiderman', email='spiderman@marvel.com', first_name='Peter', last_name='Parker'),
            User.objects.create(username='batman', email='batman@dc.com', first_name='Bruce', last_name='Wayne'),
            User.objects.create(username='wonderwoman', email='wonderwoman@dc.com', first_name='Diana', last_name='Prince'),
        ]
            # UserProfile.objects.create(user=users[0], team=marvel)  # Assign users to teams
            # UserProfile.objects.create(user=users[1], team=marvel)
            # UserProfile.objects.create(user=users[2], team=dc)
            # UserProfile.objects.create(user=users[3], team=dc)

        # Create activities
        Activity.objects.create(user=users[0], type='run', duration=30, distance=5)
        Activity.objects.create(user=users[1], type='cycle', duration=45, distance=15)
        Activity.objects.create(user=users[2], type='swim', duration=60, distance=2)
        Activity.objects.create(user=users[3], type='yoga', duration=50, distance=0)

        # Create workouts
        Workout.objects.create(name='Morning Cardio', description='A quick morning run and stretch')
        Workout.objects.create(name='Strength Training', description='Weights and resistance exercises')

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=100)
        Leaderboard.objects.create(team=dc, points=90)

        self.stdout.write(self.style.SUCCESS('Database populated with test data.'))

        # Unique index on email field is enforced by the model (unique=True)
        print('Unique index on email field enforced by model.')

# Models for reference (should be in octofit_tracker/models.py):
# class Team(models.Model):
#     name = models.CharField(max_length=100)
#     members = models.ManyToManyField(User)
#
# class Activity(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     type = models.CharField(max_length=50)
#     duration = models.IntegerField()
#     distance = models.FloatField()
#
# class Workout(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#
# class Leaderboard(models.Model):
#     team = models.ForeignKey(Team, on_delete=models.CASCADE)
#     points = models.IntegerField()
