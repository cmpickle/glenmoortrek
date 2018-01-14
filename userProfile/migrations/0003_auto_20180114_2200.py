# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0002_remove_userprofile_achievements'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='firstName',
            field=models.CharField(default=b'', max_length=20),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='lastName',
            field=models.CharField(default=b'', max_length=20),
        ),
    ]
