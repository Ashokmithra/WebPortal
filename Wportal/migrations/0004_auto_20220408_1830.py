# Generated by Django 2.2.24 on 2022-04-08 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Wportal', '0003_delete_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='standard',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default=0, max_length=100),
        ),
        migrations.AlterField(
            model_name='note',
            name='subject',
            field=models.CharField(choices=[('Tamil', 'Tamil'), ('English', 'English'), ('Maths', 'Maths'), ('Science', 'Science'), ('Social Science', 'Social Science')], default=0, max_length=100),
        ),
    ]
