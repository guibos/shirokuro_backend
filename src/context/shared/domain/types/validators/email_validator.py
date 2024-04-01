from email_validator import validate_email, EmailSyntaxError, EmailUndeliverableError


class EmailValidator:
    def _validate_email(self, email: str):
        try:
            validate_email(email)
        except EmailSyntaxError as e:
            raise NotImplementedError
        except EmailUndeliverableError as e:
            raise NotImplementedError
        except Exception as e:
            raise NotImplementedError
