# Generated by Django 3.2.6 on 2021-09-04 14:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('target', models.CharField(max_length=50)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('hitman', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.hitman')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.state')),
            ],
        ),
    ]