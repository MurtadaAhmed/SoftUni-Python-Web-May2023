from django.core.exceptions import ValidationError


def validate_that_it_starts_with_letter(value):
    if not value[0].isalpha():
        raise ValidationError("Your name must start with a letter!")


def validate_if_name_contains_only_letters(value):
    for character in value:
        if not character.isalpha():
            raise ValidationError("Fruit name should contain only letters!")

