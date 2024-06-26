# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2020-06-09 12:22
from __future__ import unicode_literals

from django.db import migrations
import multiselectfield.db.fields
import custom_fields.multiselect_with_other.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('onboarding', '0030_auto_20200618_0157'),
    ]

    operations = [
        migrations.AddField(
            model_name='userextendedprofile',
            name='function_areas',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(b'function_strategy_planning', b'Strategy and planning'), (b'function_leadership_governance', b'Leadership and governance'), (b'function_program_design', b'Program design and development'), (b'function_measurement_eval', b'Measurement, evaluation, and learning'), (b'function_stakeholder_engagement', b'External relations and partnerships'), (b'function_human_resource', b'Human resource management'), (b'function_financial_management', b'Financial management'), (b'function_fundraising', b'Fundraising and resource mobilization'), (b'function_marketing_communication', b'Marketing, communications, and PR'), (b'function_system_tools', b'Systems, tools, and processes')], max_length=269),
        ),
        migrations.AddField(
            model_name='userextendedprofile',
            name='goals',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(b'goal_contribute_to_org', b'Help improve my organization'), (b'goal_gain_new_skill', b'Develop new skills'), (b'goal_improve_job_prospect', b'Get a job'), (b'goal_relation_with_other', b'Build relationships with other nonprofit leaders')], max_length=93),
        ),
        migrations.AddField(
            model_name='userextendedprofile',
            name='hear_about_philanthropyu',
            field=custom_fields.multiselect_with_other.db.fields.MultiSelectWithOtherField(blank=True, choices=[(b'hear_about_philanthropy_partner', b'A Philanthropy University Partner (Global Giving, +Acumen or another)'), (b'hear_about_colleague_same_organization', b'A Colleague From My Organization'), (b'hear_about_friend_new_organization', b'A Friend Or Colleague (Not From My Organization)'), (b'hear_about_internet_search', b'An Internet Search'), (b'hear_about_linkedIn_advertisement', b'A LinkedIn Advertisement'), (b'hear_about_facebook_advertisement', b'A Facebook Advertisement'), (b'hear_about_twitter_not_colleague', b'Twitter (Not From A Colleague)'), (b'other', b'Other')], max_length=488),
        ),
        migrations.AddField(
            model_name='userextendedprofile',
            name='interests',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(b'interest_strategy_planning', b'Strategy and planning'), (b'interest_leadership_governance', b'Leadership and governance'), (b'interest_program_design', b'Program design and development'), (b'interest_measurement_eval', b'Measurement, evaluation, and learning'), (b'interest_stakeholder_engagement', b'External relations and partnerships'), (b'interest_human_resource', b'Human resource management'), (b'interest_financial_management', b'Financial management'), (b'interest_fundraising', b'Fundraising and resource mobilization'), (b'interest_marketing_communication', b'Marketing, communications, and PR'), (b'interest_system_tools', b'Systems, tools, and processes')], max_length=269),
        ),
        migrations.AddField(
            model_name='userextendedprofile',
            name='learners_related',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(b'learners_same_region', b'Learners from my region or country'), (b'learners_similar_oe_interest', b'Learners interested in same areas of organization effectiveness'), (b'learners_similar_org', b'Learners working for similar organizations'), (b'learners_diff_who_are_different', b'Learners who are different from me')], max_length=102),
        ),
    ]
