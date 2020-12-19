from django.db import models


class Vulnerabilities(models.Model):
    severity = models.IntegerField(default=0, choices=[(i, i) for i in range(1, 6)])
    STATUS_CHOICES = [('new', 'new'), ('reopened', 'reopened'), ('active', 'active'), ('closed', 'closed')]
    status = models.CharField(max_length=15, default='new', choices=STATUS_CHOICES)
    unremediated = models.BooleanField(default=False)
