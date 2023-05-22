from rest_framework import pagination
from rest_framework.response import Response


class CustomPagination(pagination.PageNumberPagination):
    def get_paginated_response(self, data):
        return Response(
            {
                "items": data,
                "currentPage": self.page.paginator.count,
                "lastPage": self.get_previous_link(),
            }
        )


class SalePagination(pagination.PageNumberPagination):
    def get_paginated_response(self, data):
        return Response(
            {
                "salesCards": data,
                "currentPage": self.page.paginator.count,
                "lastPage": self.get_previous_link(),
            }
        )
