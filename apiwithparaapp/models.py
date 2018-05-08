from __future__ import unicode_literals
from django.db import models
#class bubblesortModel(models.Model):
def bubblesort(a):
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a