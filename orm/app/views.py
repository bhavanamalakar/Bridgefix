from django.shortcuts import render,HttpResponse
from .models import Author , Books
from django.db import connection,reset_queries

# Helper function to count and show execured queries
def show_queries(description,queryset):
    reset_queries()        #reset query log before execution
    print(f"----{description}-------")

    # execute the queryset and access related fields

    for book in queryset:
        print(book.title,book.author.firstname)

    # count and print executed queries
    queries=len(connection.queries)
    print(f"Total Queries:{queries}")

    for i ,query in enumerate(connection.queries,start=1):
        print(f"{i}:{query['sql']}")

    print('\n')

def home(request):

    # without select related
    # without_sr_books=Books.objects.all()
    # show_queries("without select related",without_sr_books)
    # # for book in books:
    # #     print(book.title, book.author.firstname)

    # #in SQL Query
    # # select * from books
    # # select * from author WHERE id=author_id

    # #with select related
    # with_sr_books=Books.objects.select_related('author').all()
    # show_queries("with select related",with_sr_books)

    # # for book in books:
    # #     print(book.title , book.author.firstname)

    # PREFETCHED RELATED

    # without PREFETCHED related
    without_PR_books=Books.objects.all()
    show_queries("without PREFETCHEDrelated",without_PR_books)
    # for book in books:
    #     print(book.title, book.author.firstname)

    #in SQL Query
    # select * from books
    # select * from author WHERE id=author_id

    #with PREFETCHED related
    with_PR_books=Books.objects.prefetch_related('author').all()
    show_queries("with PREFETCHED related",with_PR_books)

    # for book in books:
    #     print(book.title , book.author.firstname)


    return HttpResponse("Hello,From HOme View")
