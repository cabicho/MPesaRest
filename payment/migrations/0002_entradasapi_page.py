# Generated by Django 2.1.3 on 2018-12-22 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entradasapi',
            name='page',
            field=models.CharField(default='Payment', max_length=20),
            preserve_default=False,
        ),
    ]