# Generated by Django 3.1.3 on 2020-12-19 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vulnerabilities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('severity', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=0)),
                ('status', models.CharField(choices=[('new', 'new'), ('reopened', 'reopened'), ('active', 'active'), ('closed', 'closed')], default='new', max_length=15)),
                ('unremediated', models.BooleanField(default=False)),
            ],
        ),
    ]