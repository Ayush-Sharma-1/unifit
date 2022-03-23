# Generated by Django 2.1.5 on 2022-03-22 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uni_fit', '0017_auto_20220322_2234'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='university',
            name='FavouriteUnversity',
        ),
        migrations.AddField(
            model_name='university',
            name='FavouriteUnversity',
            field=models.ManyToManyField(blank=True, default=None, related_name='favourite', to='uni_fit.Users'),
        ),
    ]
