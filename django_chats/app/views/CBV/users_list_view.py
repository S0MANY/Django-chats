from django.db.models import Q
from django.views.generic import ListView

from users.models import CustomUser


class UsersListView(ListView):

    model = CustomUser
    template_name = "app/users.html"

    def get_queryset(self):
        queryset = (
            CustomUser.objects.exclude(first_name__isnull=True)
            .exclude(first_name__exact="")
            .exclude(is_superuser=True)
        )
        query = self.request.GET.get("q")

        if query:
            queryset = queryset.filter(
                Q(first_name__icontains=query)
                | Q(last_name__icontains=query)
                | Q(username__icontains=query)
                | Q(first_name__icontains=query.capitalize())
                | Q(last_name__icontains=query.capitalize())
                | Q(username__icontains=query.capitalize())
            )

        return queryset
