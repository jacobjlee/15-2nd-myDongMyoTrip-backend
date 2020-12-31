# Generated by Django 3.1.4 on 2020-12-30 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accommodation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.CharField(max_length=500)),
                ('number_of_guest', models.IntegerField(default=1)),
                ('star_rating', models.DecimalField(decimal_places=2, max_digits=5)),
                ('check_in', models.DateField()),
                ('check_out', models.DateField()),
                ('address', models.CharField(max_length=100)),
                ('is_immediate_confirmation', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'accommodations',
            },
        ),
        migrations.CreateModel(
            name='AccommodationDormitory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'accommodation_dormitories',
            },
        ),
        migrations.CreateModel(
            name='AccommodationFacility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'accommodation_facilities',
            },
        ),
        migrations.CreateModel(
            name='AccommodationImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.CharField(max_length=2000)),
            ],
            options={
                'db_table': 'accommodation_images',
            },
        ),
        migrations.CreateModel(
            name='AccommodationPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_payment_status', models.BooleanField(default=False)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=15)),
            ],
            options={
                'db_table': 'accommodation_payments',
            },
        ),
        migrations.CreateModel(
            name='AccommodationRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'accommodation_rooms',
            },
        ),
        migrations.CreateModel(
            name='AccommodationService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'accommodation_services',
            },
        ),
        migrations.CreateModel(
            name='AccommodationTheme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'accommodation_themes',
            },
        ),
        migrations.CreateModel(
            name='AgeGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'age_groups',
            },
        ),
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'coupons',
            },
        ),
        migrations.CreateModel(
            name='Dormitory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'dormitories',
            },
        ),
        migrations.CreateModel(
            name='FreeService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'free_services',
            },
        ),
        migrations.CreateModel(
            name='GeneralRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'general_rooms',
            },
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'payment_methods',
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('date_of_birth', models.DateField()),
                ('estimate_arrival_time', models.TimeField()),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=15)),
                ('is_privcy_agreement', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'reservations',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('context', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('star_rating', models.DecimalField(decimal_places=1, max_digits=5)),
                ('image_url', models.CharField(max_length=2000)),
            ],
            options={
                'db_table': 'reviews',
            },
        ),
        migrations.CreateModel(
            name='RoomAmenity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'room_amenities',
            },
        ),
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'db_table': 'room_types',
            },
        ),
        migrations.CreateModel(
            name='RoomTypeAmenity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'room_type_amenities',
            },
        ),
        migrations.CreateModel(
            name='RoomTypeImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.CharField(max_length=2000)),
            ],
            options={
                'db_table': 'room_type_images',
            },
        ),
        migrations.CreateModel(
            name='SharedFacility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'shared_facilities',
            },
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'themes',
            },
        ),
        migrations.CreateModel(
            name='TravelType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'travel_types',
            },
        ),
        migrations.CreateModel(
            name='UserCoupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coupon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accommodation.coupon')),
                ('reservation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accommodation.reservation')),
            ],
            options={
                'db_table': 'user_coupons',
            },
        ),
    ]
