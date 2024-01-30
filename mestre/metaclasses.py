from datetime import datetime
import re

class ValidationError(Exception):
    pass

class Field:
    def __init__(self, **kwargs):
        self.default = kwargs.get('default')
        self.blank = kwargs.get('blank', False)
        self.value = None

    def set_value(self, value):
        self.value = value

    def get_value(self):
        if self.value is not None:
            return self.value
        return self.default

    def validate(self):
        if self.get_value() is None and not self.blank:
            raise ValidationError(f"{self.name} field value is None, but field is not blank")

class CharField(Field):
    def __init__(self, min_length=0, max_length=None, **kwargs):
        super().__init__(**kwargs)
        self.min_length = min_length
        self.max_length = max_length

    def validate(self):
        super().validate()
        if not isinstance(self.value, str):
            raise ValidationError("Value is not a string")
        if len(self.value) < self.min_length or (self.max_length is not None and len(self.value) > self.max_length):
            raise ValidationError("Value length is out of range")

class IntegerField(Field):
    class IntegerField(Field):
        def __init__(self, min_value=None, max_value=None, **kwargs):
            super().__init__(**kwargs)
            self.min_value = min_value
            self.max_value = max_value

        def validate(self):
            super().validate()
            if self.value is not None:
                if not isinstance(self.value, int):
                    try:
                        self.value = int(self.value)
                    except ValueError:
                        raise ValidationError("Value cannot be converted to an integer")
                if (self.min_value is not None and self.value < self.min_value) or (self.max_value is not None and self.value > self.max_value):
                    raise ValidationError("Value is out of range")
class BooleanField(Field):
    def validate(self):
        super().validate()
        if not isinstance(self.value, bool):
            raise ValidationError("Value is not a boolean")

class DateTimeField(Field):
    def __init__(self, auto_now=False, **kwargs):
        super().__init__(**kwargs)
        self.auto_now = auto_now
        if self.auto_now and self.value is None:
            self.value = datetime.now()

    def validate(self):
        super().validate()
        if not isinstance(self.value, datetime):
            raise ValidationError("Value is not a datetime")

class EmailField(CharField):
    def validate(self):
        super().validate()
        if not re.match(r"[^@]+@[^@]+\.[^@]+", self.value):
            raise ValidationError("Value is not a valid email address")

class ModelMeta(type):
    def __new__(mcs, name, bases, attrs):
        new_attrs = {}
        for attr_name, attr_value in attrs.items():
            if isinstance(attr_value, Field):
                attr_value.name = attr_name
            new_attrs[attr_name] = attr_value
        return super().__new__(mcs, name, bases, new_attrs)

class Model(metaclass=ModelMeta):
    def __init__(self, **kwargs):
        for attr_name, attr_value in kwargs.items():
            field = getattr(self, attr_name, None)
            if isinstance(field, Field):
                field.value = attr_value

    def validate(self):
        for attr_name in dir(self):
            field = getattr(self, attr_name)
            if isinstance(field, Field):
                field.validate()

def test_model():
    class User(Model):
        first_name = CharField(max_length=30, default='Adam')
        last_name = CharField(max_length=50)
        email = EmailField()
        is_verified = BooleanField(default=False)
        date_joined = DateTimeField(auto_now=True)
        age = IntegerField(min_value=5, max_value=120, blank=True)

    user = User(first_name='Liam', last_name='Smith', email='liam@example.com')
    user.validate()

    assert user.date_joined is not None, "date_joined should be auto set to now"
    assert user.is_verified == False, "is_verified should be False by default"

    user.age = 256
    try:
        user.validate()
    except ValidationError:
        pass
    else:
        assert False, "ValidationError should be raised when age is out of range"

    user2 = User()
    try:
        user2.validate()
    except ValidationError:
        pass
    else:
        assert False, "ValidationError should be raised when mandatory fields are missing"

if __name__ == "__main__":
    test_model()