from __future__ import unicode_literals
from django.db import models
#class bubblesortModel(models.Model):
def bubblesort(a):
    idx = 0
    i = 0
    smallest = 0
    for i in range(0, len(a)):
        smallest = min(a[i:])
        idx = a.index(smallest)
        a[i], a[idx] = a[idx], a[i]
    return a