# Generated by Django 2.1.1 on 2018-10-18 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0007_auto_20181019_0045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='justaminute',
            name='member_1',
        ),
        migrations.RemoveField(
            model_name='justaminute',
            name='number_of_members',
        ),
        migrations.RemoveField(
            model_name='justaminute',
            name='team_name',
        ),
        migrations.RemoveField(
            model_name='posterandpresentation',
            name='member_1',
        ),
        migrations.RemoveField(
            model_name='posterandpresentation',
            name='number_of_members',
        ),
        migrations.RemoveField(
            model_name='posterandpresentation',
            name='team_name',
        ),
        migrations.RemoveField(
            model_name='postermaking',
            name='member_3',
        ),
        migrations.RemoveField(
            model_name='postermaking',
            name='member_4',
        ),
        migrations.AlterField(
            model_name='codewar',
            name='event_id',
            field=models.CharField(default='CSE01', max_length=5),
        ),
        migrations.AlterField(
            model_name='codewar',
            name='event_name',
            field=models.CharField(default='CODE WAR', max_length=20),
        ),
        migrations.AlterField(
            model_name='codewar',
            name='member_1',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='codewar',
            name='member_2',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='cosmetic',
            name='event_id',
            field=models.CharField(default='Bph02', max_length=5),
        ),
        migrations.AlterField(
            model_name='cosmetic',
            name='event_name',
            field=models.CharField(default='COSMETICS', max_length=20),
        ),
        migrations.AlterField(
            model_name='guessthebond',
            name='event_id',
            field=models.CharField(default='CIV01', max_length=5),
        ),
        migrations.AlterField(
            model_name='guessthebond',
            name='event_name',
            field=models.CharField(default='GUESS THE BOND?', max_length=30),
        ),
        migrations.AlterField(
            model_name='guessthebond',
            name='member_1',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='guessthebond',
            name='member_2',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='industrialcasestudy',
            name='event_id',
            field=models.CharField(default='CH01', max_length=5),
        ),
        migrations.AlterField(
            model_name='industrialcasestudy',
            name='event_name',
            field=models.CharField(default='INDUSTRIAL CASE STUDY', max_length=30),
        ),
        migrations.AlterField(
            model_name='industrialcasestudy',
            name='member_1',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='industrialcasestudy',
            name='member_2',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='justaminute',
            name='event_id',
            field=models.CharField(default='BT01', max_length=5),
        ),
        migrations.AlterField(
            model_name='justaminute',
            name='event_name',
            field=models.CharField(default='JUST A MINUTE', max_length=20),
        ),
        migrations.AlterField(
            model_name='karyaniti',
            name='event_id',
            field=models.CharField(default='MBA01', max_length=5),
        ),
        migrations.AlterField(
            model_name='karyaniti',
            name='event_name',
            field=models.CharField(default='KARYANITI', max_length=20),
        ),
        migrations.AlterField(
            model_name='karyaniti',
            name='member_1',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='karyaniti',
            name='member_2',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='karyaniti',
            name='member_3',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='karyaniti',
            name='member_4',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='mindfizz',
            name='event_id',
            field=models.CharField(default='ECE01', max_length=5),
        ),
        migrations.AlterField(
            model_name='mindfizz',
            name='event_name',
            field=models.CharField(default='MIND FIZZ', max_length=20),
        ),
        migrations.AlterField(
            model_name='mindfizz',
            name='member_1',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='mindfizz',
            name='member_2',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='mindfizz',
            name='member_3',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='mindfizz',
            name='member_4',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='posterandpresentation',
            name='event_id',
            field=models.CharField(default='MCA02', max_length=5),
        ),
        migrations.AlterField(
            model_name='posterandpresentation',
            name='event_name',
            field=models.CharField(default='POSTER & PRESENTATIONS', max_length=40),
        ),
        migrations.AlterField(
            model_name='postermaking',
            name='event_id',
            field=models.CharField(default='Bph01', max_length=5),
        ),
        migrations.AlterField(
            model_name='postermaking',
            name='event_name',
            field=models.CharField(default='POSTER MAKING', max_length=20),
        ),
        migrations.AlterField(
            model_name='postermaking',
            name='member_1',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='postermaking',
            name='member_2',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='roborace',
            name='event_id',
            field=models.CharField(default='EN01', max_length=5),
        ),
        migrations.AlterField(
            model_name='roborace',
            name='event_name',
            field=models.CharField(default='ROBO RACE', max_length=20),
        ),
        migrations.AlterField(
            model_name='roborace',
            name='member_1',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='roborace',
            name='member_2',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='roborace',
            name='member_3',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='roborace',
            name='member_4',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='robosoccer',
            name='event_id',
            field=models.CharField(default='ME02', max_length=5),
        ),
        migrations.AlterField(
            model_name='robosoccer',
            name='event_name',
            field=models.CharField(default='ROBO SOCCER', max_length=20),
        ),
        migrations.AlterField(
            model_name='robosoccer',
            name='member_1',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='robosoccer',
            name='member_2',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='robosoccer',
            name='member_3',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='robosoccer',
            name='member_4',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='robosoccer',
            name='number_of_members',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='startupmaster',
            name='event_id',
            field=models.CharField(default='EN02', max_length=5),
        ),
        migrations.AlterField(
            model_name='startupmaster',
            name='event_name',
            field=models.CharField(default='START UP MASTER', max_length=30),
        ),
        migrations.AlterField(
            model_name='startupmaster',
            name='member_1',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='startupmaster',
            name='member_2',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='technicalquiz',
            name='event_id',
            field=models.CharField(default='MCA01', max_length=5),
        ),
        migrations.AlterField(
            model_name='technicalquiz',
            name='event_name',
            field=models.CharField(default='TECHNICAL QUIZ', max_length=20),
        ),
        migrations.AlterField(
            model_name='technicalquiz',
            name='member_1',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='technicalquiz',
            name='member_2',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='webdesigning',
            name='event_id',
            field=models.CharField(default='IT01', max_length=5),
        ),
        migrations.AlterField(
            model_name='webdesigning',
            name='event_name',
            field=models.CharField(default='WEB DESIGNING', max_length=20),
        ),
        migrations.AlterField(
            model_name='webdesigning',
            name='member_1',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='webdesigning',
            name='member_2',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
    ]