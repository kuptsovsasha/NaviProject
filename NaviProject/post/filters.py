import django_filters

from NaviProject.post.models import Like


class LikesAnalyticsFilters(django_filters.FilterSet):
    date_from = django_filters.DateFilter(field_name="created_at", lookup_expr="gte")
    date_to = django_filters.DateFilter(field_name="created_at", lookup_expr="lte")

    class Meta:
        model = Like
        fields = (
            "date_from",
            "date_to",
        )
