import re
import pytz
from logging import getLogger

from dateutil.relativedelta import relativedelta
from datetime import datetime
from difflib import SequenceMatcher
import pycountry

from django.db.models.functions import Length

from onboarding.constants import ORG_SEARCH_TERM_LENGTH
from onboarding.models import Organization

from openedx.core.djangoapps.site_configuration import helpers as configuration_helpers

utc = pytz.UTC
log = getLogger(__name__)


def get_country_name(country_code):
    """
    Returns the country name for a given ISO 3166-1 alpha-2 country code.

    Args:
        country_code (str): The ISO 3166-1 alpha-2 country code.

    Returns (str):
        The name of the country or an empty string if the country code is invalid.
    """
    try:
        return pycountry.countries.get(alpha_2=country_code).name
    except AttributeError:
        log.exception(f"Can't resolve the {country_code!r} country code into the country name.")
        return ''


def get_current_utc_date():
    """
    :return: current date in utc
    """
    return utc.localize(datetime.now())


def get_diff_from_current_date(submission_date):
    """
    :param: submission_date
    :return: relative delta of python aware(UTC) current datetime and submission date
    """
    return relativedelta(get_current_utc_date(), submission_date)


def its_been_year(submission_date):
    """
    :param submission_date:
    :return: True if latest submission is an year ago else False
    """
    time_delta = get_diff_from_current_date(submission_date)
    return time_delta.years >= 1


def its_been_year_month(submission_date):
    """
    :param submission_date:
    :return: True if latest submission is an year and month ago else False
    """
    time_delta = get_diff_from_current_date(submission_date)
    return time_delta.years >= 1 and time_delta.months >= 1


def its_been_year_three_month(submission_date):
    """
    :param submission_date:
    :return: True if latest submission is an year and three months ago else False
    """
    time_delta = get_diff_from_current_date(submission_date)
    return time_delta.years >= 1 and time_delta.months >= 3


def its_been_year_six_month(submission_date):
    """
    :param submission_date:
    :return: True if latest submission is an year and six months ago else False
    """
    time_delta = get_diff_from_current_date(submission_date)
    return time_delta.years >= 1 and time_delta.months >= 6


def get_str_match_ratio(str1, str2):
    """
    Return matching percentage of two strings.
    """
    str1 = re.sub('[^A-Za-z0-9]+', '', str1)
    str2 = re.sub('[^A-Za-z0-9]+', '', str2)
    return SequenceMatcher(None, str1, str2).ratio()


def get_close_matching_orgs_with_suggestions(request, query):
    """
    Find list of orgs which are very close to a searched string.
    """
    data = {}

    organizations = Organization.objects.filter(label__istartswith=query)
    if len(query) == ORG_SEARCH_TERM_LENGTH:
        organizations = organizations.annotate(label_length=Length('label')).filter(label_length=ORG_SEARCH_TERM_LENGTH)

    for organization in organizations:
        match_ratio = get_str_match_ratio(query.lower(), organization.label.lower())
        is_suggestion = True if re.match(query, organization.label, re.I) else False
        is_matched = True if match_ratio >= configuration_helpers.get_value('org_search_ratio', 0) else False
        if is_suggestion or is_matched:
            data[organization.label.lower()] = {
                'id': organization.id,
                'label': organization.label,
                'is_admin_assigned': True if organization.admin else False,
                'is_current_user_admin': True if organization.admin == request.user else False,
                'admin_email': organization.admin.email if organization.admin else 'Administrator not assigned yet.',
                'country': get_country_name(organization.country) if organization.country else '',
                'is_matched': is_matched,
                'is_suggestion': is_suggestion,
                'has_affiliated_partner': organization.has_affiliated_partner,
                'total_employees': organization.total_employees,
                'org_type': organization.org_type,
                'is_organization_registered': organization.is_organization_registered
            }

    return data
