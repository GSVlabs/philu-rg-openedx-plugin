from xblock.fields import Scope
from xmodule.course_metadata_utils import DEFAULT_START_DATE
from xmodule.fields import Date
from xmodule import course_block

# .. override_object: xmodule.course_block.CourseFields
# .. override_implementation: MonkeyPatching
# .. override_description: fix for main page course listing
#    The course is visible on the main page right after creation.
#
#    So anonymous users can see them and access the course about page
#    for the courses without valid data (e.g. they will see the default
#    course overview)
#
#    When courses list filtering is processed it checks the `see_exists`
#    permission for the anonymous user.
#    Actually, `see_exists` means `can_load` OR `can_enroll`.
#
#    `can_load` is False in our case because the course start in the future.
#
#    But `can_enroll` returns True because the course's enrollment_start
#    and enrollment_end dates are blank:
#    ```
#    enrollment_start = courselike.enrollment_start or datetime.min.replace(tzinfo=UTC)
#    enrollment_end = courselike.enrollment_end or datetime.max.replace(tzinfo=UTC)
#    if enrollment_start < now < enrollment_end:
#        debug("Allow: in enrollment period")
#        return ACCESS_GRANTED
#    ```
#
#    Set the enrollment_start the same as a course start by default
#
#    - this fix will work for the course catalog page when the course
#    discovery is disabled (FEATURES['ENABLE_COURSE_DISCOVERY'] = False)
#    - I wonder why DEFAULT_START_DATE is hardcoded (1 Jan 2030)?
#    How and when is it updated?
# .. override_impact_service: lms & studio
# .. override_creation_date: 2023-02-09
# .. override_fix_to_upstream: https://github.com/openedx/edx-platform/pull/30954

# Make '_' a no-op so we can scrape strings. Using lambda instead of
#  `django.utils.translation.ugettext_noop` because Django cannot be imported in this file
_ = lambda text: text

CourseFieldsWithStartDate = course_block.CourseFields
CourseFieldsWithStartDate.enrollment_start = Date(
        help=_("Date that enrollment for this class is opened"),
        default=DEFAULT_START_DATE,
        scope=Scope.settings
    )

# overriding CourseFields class with the new attribute
course_block.CourseFields = CourseFieldsWithStartDate
