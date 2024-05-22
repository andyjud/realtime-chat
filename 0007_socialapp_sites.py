from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('socialaccount', '0006_alter_socialaccount_extra_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialapp',
            name='sites',
            field=models.ManyToManyField(blank=True, to='sites.site'),
        ),
    ]
