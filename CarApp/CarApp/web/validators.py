from django.core import exceptions


def validate_only_alphanumeric(value):
    for ch in value:
        if not ch.isalnum() and ch != '_':
            raise exceptions.ValidationError('Ensure this value contains only letters, numbers, and underscore.')


def validate_min_chars(value):
    if len(value) < 2:
        raise exceptions.ValidationError('The username must be a minimum of 2 chars')


def validate_year_included(value):
    if not 1980 <= int(value) <= 2049:
        raise exceptions.ValidationError('Year must be between 1980 and 2049')

