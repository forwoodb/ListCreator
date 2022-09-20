# Generated by Django 3.2.7 on 2022-05-06 20:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lists', '0002_listitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='listitem',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='listname',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='listitem',
            name='list',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lists.listname'),
        ),
    ]