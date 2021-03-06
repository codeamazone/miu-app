# Generated by Django 3.1.7 on 2021-03-12 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idea', models.CharField(max_length=200)),
                ('kind', models.CharField(choices=[('VIS', 'Vision'), ('TRY', 'Try something'), ('PRO', 'Project')], default='VIS', max_length=3)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('NO', 'Pending'), ('ON', 'In Progress'), ('OK', 'Completed')], default='NO', max_length=2)),
            ],
        ),
    ]
