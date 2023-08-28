from rest_framework.pagination import CursorPagination


class ContributorListPagination(CursorPagination):
    page_size = 4
    ordering = 'time_created'
    cursor_query_param = 'record'


class ProjectListPagination(CursorPagination):
    page_size = 4
    ordering = 'time_created'
    cursor_query_param = 'record'


class IssueListPagination(CursorPagination):
    page_size = 2
    ordering = 'time_created'
    cursor_query_param = 'record'


class CommentListPagination(CursorPagination):
    page_size = 6
    ordering = 'time_created'
    cursor_query_param = 'record'
