from rest_framework.pagination import PageNumberPagination, CursorPagination

# class SubTaskPagination(PageNumberPagination):
#     page_size = 5


class CustomCursorPagination(CursorPagination):
    page_size = 5
    ordering = 'id'