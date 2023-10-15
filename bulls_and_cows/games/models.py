from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

UserModel = get_user_model()


class GamesRanking(models.Model):
    player = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    start_date_time = models.DateTimeField(auto_now=True)

    end_date_time = models.DateTimeField(
        null=True,
        blank=True
    )

    time_diff = models.DurationField(
        null=True,
        blank=True
    )

    is_finished = models.BooleanField(
        default=False,
    )

    passes = models.IntegerField(
        blank=True,
        null=True,
    )

    def finish_game(self, passes):
        if not self.is_finished:
            self.is_finished = True
            self.end_date_time = timezone.now()
            self.time_diff = self.end_date_time - self.start_date_time
            self.passes = passes
            self.save()
