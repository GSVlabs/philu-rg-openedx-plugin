import pytz
from logging import getLogger

from dateutil.relativedelta import relativedelta
from datetime import datetime


utc = pytz.UTC
log = getLogger(__name__)


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
