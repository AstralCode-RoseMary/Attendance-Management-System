# Generated by Django 5.0.4 on 2024-05-08 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('dept_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('dept_name', models.CharField()),
                ('dept_dis', models.CharField()),
                ('dept_parent', models.IntegerField(null=True)),
                ('dept_level', models.IntegerField()),
                ('create_on', models.DateField()),
                ('create_by', models.CharField()),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('feedback_id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=100)),
            ],
        ),

        migrations.CreateModel(
            name='Leaveform',
            fields=[
                ('leave_form_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('lead', models.CharField(max_length=100)),
                ('leave_type', models.CharField(max_length=100)),
                ('reason', models.TextField(max_length=250)),
            ],
        ),

        migrations.CreateModel(
            name='Register',
            fields=[
                ('register_id', models.AutoField(primary_key=True, serialize=False)),
                ('fullname', models.CharField(max_length=100)),
                ('per_address', models.CharField(max_length=100)),
                ('cur_address', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.EmailField(default='no-reply@example.com', max_length=254)),
                ('dob', models.DateField()),
                ('department', models.CharField(max_length=20)),
                ('seating_location', models.CharField(max_length=20)),
                ('date_of_join', models.DateField()),
                ('date_of_confirmation', models.DateField()),
                ('employee_status', models.CharField(max_length=10)),
                ('work_phone', models.CharField(max_length=10)),
                ('experience', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Timeslot',
            fields=[
                ('time_id', models.AutoField(primary_key=True, serialize=False)),
                ('cdate', models.DateField()),
                ('checkin', models.TimeField()),
                ('checkout', models.TimeField()),
            ],
        ),
    ]
