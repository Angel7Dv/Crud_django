from django.shortcuts import render

"""use onClick and fech + only JavaScript without jinja2 get all tags """

def board(request):
    return render(request, 'board/board.html')