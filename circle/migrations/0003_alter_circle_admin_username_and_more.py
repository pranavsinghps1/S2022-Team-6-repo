# Generated by Django 4.0.2 on 2022-03-01 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_alter_userdata_dob'),
        ('circle', '0002_alter_circleuser_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='circle',
            name='admin_username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.userdata'),
        ),
        migrations.AlterField(
            model_name='circlepolicy',
            name='policy_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='circle.policy'),
        ),
        migrations.AlterUniqueTogether(
            name='circlepolicy',
            unique_together={('circle_id', 'policy_id')},
        ),
    ]
