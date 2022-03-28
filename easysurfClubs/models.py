from django.db import models

class Club(models.Model):
    '''Model for clubs/committees (we'll just call them clubs in the code.) Users can only be apart of one club in order to make this easier due to limited time.'''
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=500)    
    members = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
    
    def get_club_member_count(self):
        return self.members