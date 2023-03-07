# Generated by Django 4.1.5 on 2023-02-13 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_channelforapi_limit_channelforapi_limit_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='engr_department',
            fields=[
                ('departmentid', models.IntegerField(primary_key=True, serialize=False)),
                ('departmentname', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='engr_leveleducation',
            fields=[
                ('levelid', models.IntegerField(primary_key=True, serialize=False)),
                ('levelname', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='engr_titlename',
            fields=[
                ('titleid', models.IntegerField(primary_key=True, serialize=False)),
                ('title_name_t', models.CharField(max_length=50)),
                ('title_name_e', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='per_person',
            fields=[
                ('personid', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('title', models.IntegerField()),
                ('fname_t', models.CharField(max_length=255)),
                ('lname_t', models.CharField(max_length=255)),
                ('fname_e', models.CharField(max_length=255)),
                ('lname_e', models.CharField(max_length=255)),
                ('department', models.IntegerField()),
                ('title_academic', models.IntegerField()),
                ('ad_user', models.CharField(max_length=15)),
            ],
        ),
        migrations.DeleteModel(
            name='student',
        ),
        migrations.AlterField(
            model_name='instructor',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.engr_department'),
        ),
        migrations.DeleteModel(
            name='department',
        ),
    ]
