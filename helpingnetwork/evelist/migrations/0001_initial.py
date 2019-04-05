# Generated by Django 2.2 on 2019-04-04 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organization', '0001_initial'),
        ('volunteer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('date', models.DateTimeField()),
                ('eventprofileImage', models.ImageField(default='default.jpg', upload_to='eventprofileImage')),
            ],
        ),
        migrations.CreateModel(
            name='EventCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invite_reason', models.CharField(max_length=64)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evelist.Event')),
                ('volunteer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='volunteer.Volunteer')),
            ],
        ),
        migrations.CreateModel(
            name='EventImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='eventimages')),
                ('i_event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evelist.Event')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evelist.EventCategory'),
        ),
        migrations.AddField(
            model_name='event',
            name='organizer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.Organization'),
        ),
        migrations.AddField(
            model_name='event',
            name='venue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='volunteer.City'),
        ),
        migrations.AddField(
            model_name='event',
            name='volunteers',
            field=models.ManyToManyField(through='evelist.Signup', to='volunteer.Volunteer'),
        ),
    ]
