from rest_framework.pagination import CursorPagination


class UserListPagination(CursorPagination):
    page_size = 3
    ordering = 'time_created'
    cursor_query_param = 'record'
