# Generated by Django 3.2.4 on 2021-06-28 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=25)),
                ('agegroup', models.CharField(choices=[('KIDS', 'Kids'), ('ADULTS', 'adults')], default='kids', max_length=30)),
                ('specialoffer', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Myntra',
            fields=[
                ('MID', models.IntegerField(primary_key=True, serialize=False)),
                ('pname', models.CharField(max_length=25)),
                ('price', models.IntegerField()),
                ('discount', models.IntegerField()),
                ('CAT_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='online.category')),
            ],
        ),
        migrations.CreateModel(
            name='Flipkart',
            fields=[
                ('FID', models.IntegerField(primary_key=True, serialize=False)),
                ('pname', models.CharField(max_length=25)),
                ('price', models.IntegerField()),
                ('discount', models.IntegerField()),
                ('CAT_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='online.category')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('Cid', models.IntegerField(primary_key=True, serialize=False)),
                ('cname', models.CharField(max_length=25)),
                ('phone', models.BigIntegerField()),
                ('address', models.TextField(max_length=100)),
                ('FID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='online.flipkart')),
                ('MID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='online.myntra')),
            ],
        ),
    ]
