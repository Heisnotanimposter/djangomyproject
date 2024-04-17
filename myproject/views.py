#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


from django.shortcuts import render

def my_view(request):
    items = ['사과', '바나나', '오렌지']
    return render(request, 'mytemplate.html', {'items': items})


if __name__ == "__main__":
    main()
