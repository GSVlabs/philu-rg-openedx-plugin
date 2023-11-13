"""Override for Gradebook view"""
from common.djangoapps.student.models import CourseEnrollment


# pylint: disable=unused-argument
def _get_user_count(original_func, self, query_args, cache_time=3600, annotations=None):
    """
    This method removes caching from the original function.
    """
    queryset = CourseEnrollment.objects
    if annotations:
        queryset = queryset.annotate(**annotations)
    queryset = queryset.filter(*query_args)

    user_count = queryset.count()

    return user_count
