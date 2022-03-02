# Generated by Django 4.0.2 on 2022-03-02 01:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_alter_userdata_dob'),
        ('circle', '0004_circle_pending_request'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestCircle',
            fields=[
                ('request_id', models.AutoField(primary_key=True, serialize=False)),
                ('circle_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='circle.circle')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.userdata')),
            ],
            options={
                'unique_together': {('circle_id', 'username')},
            },
        ),
    ]