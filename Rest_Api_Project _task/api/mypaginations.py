from rest_framework.pagination import PageNumberPagination
# from rest_framework.pagination import CursorPagination
from rest_framework.pagination import LimitOffsetPagination

class MyPageNumberPagination(PageNumberPagination):
   page_size = 1
   page_query_param = 'p' # pagenumber pagination we use ?page=2 now we can use ?p=2
   page_size_query_param = 'records' # here we can give how muc record we can define how much we can show data to perticular page .
   max_page_size = 7  # cleint can seee 7 record only on single page 
   last_page_strings = ("end", ) # suppose if we had write last now we can write end as we had change string

# class MyCursorPagination(CursorPagination):
#    page_size = 3
#    ordering = 'title'  # we use ordering because of time stem[p issue that is crwate at feild (field error)
#    cursor_query_param = 'cu'
   

class MyLimitOffsetPagination(LimitOffsetPagination):
   default_limit = 2
   limit_query_param = 'mylimit'
   offset_query_param = 'myoffset'
   max_limit = 3