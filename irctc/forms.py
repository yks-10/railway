from django.forms import  *
from . models import *

class TrainForm(ModelForm):
    class Meta:
        model=Train
        fields=['starting','ending','date']