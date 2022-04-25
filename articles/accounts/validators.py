from django.core.exceptions import ValidationError


class OneNumberPasswordValidator:

    def validate(self, password, user=None):
        if not any(symbol.isdigit() for symbol in password):
            raise ValidationError(
                'This password must contain at least one number.',
                code='password_has_not_numbers',
            )

    def get_help_text(self):
        return 'Your password must contain at least one number.'

class OneLetterPasswordValidator:

    def validate(self, password, user=None):
        if not any(symbol.isalpha() for symbol in password):
            raise ValidationError(
                'This password must contain at least one letter.',
                code='password_has_not_letters',
            )

    def get_help_text(self):
        return 'Your password must contain at least one letter.'