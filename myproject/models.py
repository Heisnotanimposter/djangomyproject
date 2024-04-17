#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


class MyModel(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()

    class Meta:
        db_table = 'your_table_name'

if __name__ == "__main__":
    main()
