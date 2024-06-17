from django.db import migrations


class Migration(migrations.Migration):

    def update_total_employees(apps, schema_editor):
        _levels = {
            "1-ONLY": 1,
            "2-5": 2,
            "6-10": 3,
            "11-20": 4,
            "21-50": 5,
            "51-100": 6,
            "101-200": 7,
            "201-501": 8,
            "501-1,000": 9,
            "1,000+": 10,
            "NA": 11,
        }

        TotalEmployee = apps.get_model('onboarding', 'TotalEmployee')

        # temporary values ​​for order field
        for i, code in enumerate(_levels.keys()):
            TotalEmployee.objects.filter(code=code).update(order=100 + i)

        for code, order in _levels.items():
            TotalEmployee.objects.filter(code=code).update(order=order)

    dependencies = [
        ('onboarding', '0036_auto_20240606_1355'),
    ]

    operations = [
        migrations.RunPython(update_total_employees),
    ]
