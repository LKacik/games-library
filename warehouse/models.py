from django.db import models

# Create your models here.


class Games(models.Model):
    game_id = models.AutoField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=64, default='Cannon Fodder')
    slug = models.SlugField(default='cannon-fodder')
    description = models.TextField(default="From a queue of some 360 'eager' conscripts waiting to go to war,"
                                           " a team of up to six will 'volunteer' for each new mission. Encourage your"
                                           " soldiers to shoot anything that moves, throw grenades, fire bazookas,"
                                           " drive tanks, fly choppers, split up and do their own thing... and die..."
                                           "Guide your no-hoper's troop straight through deadly missions. And if you"
                                           " lose some of them? There's more where that came from...Action-driven,"
                                           " fast-paced classic arcade gameplay A mix of tactical insight and"
                                           " fast reflexes required, a good micro would be a plus"
                                           " War has never been so much fun!")
    platform = models.CharField(max_length=192, default='Commodore / Amiga')
    image = models.ImageField(upload_to=None)
    released = models.DateField(default='1992-11-28')
    developers = models.CharField(max_length=64, default='Sensible Software')



