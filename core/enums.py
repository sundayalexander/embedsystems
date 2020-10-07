from django.db.models import PositiveSmallIntegerField


class CustomEnum(object):

    class Enum(object):
        name = None
        value = None
        type = None

        def __init__(self, name, value, type):
            self.key = name
            self.name = name
            self.value = value
            self.type = type

        def __str__(self):
            return self.name

        def __repr__(self):
            return self.name

        def __eq__(self, other):
            if other is None:
                return False
            if isinstance(other, CustomEnum.Enum):
                return self.value == other.value
            raise TypeError

    @classmethod
    def choices(cls):
        attrs = [a for a in cls.__dict__.keys() if a.isupper()]
        values = [
            (cls.__dict__[v], CustomEnum.Enum(
                v, cls.__dict__[v], cls).__str__()) for v in attrs]
        return sorted(values, key=lambda x: x[0])

    @classmethod
    def default(cls):
        """
        Returns default value, which is the first one by default.
        Override this method if you need another default value.
        """
        return cls.choices()[0][0]

    @classmethod
    def field(cls, **kwargs):
        """
        A shortcut for
        Usage:
            class MyModelStatuses(CustomEnum):
                UNKNOWN = 0
            class MyModel(Model):
                status = MyModelStatuses.field(label='my status')
        """
        field = PositiveSmallIntegerField(choices=cls.choices(), default=cls.default(), **kwargs)
        field.enum = cls
        return field

    @classmethod
    def get(cls, value):
        if type(value) is int:
            try:
                return [
                    CustomEnum.Enum(k, v, cls) for k, v in cls.__dict__.items() if k.isupper() and v == value][0]
            except Exception:
                return None
        else:
            try:
                key = value.upper()
                return CustomEnum.Enum(key, cls.__dict__[key], cls)
            except Exception:
                return None

    @classmethod
    def key(cls, key):
        try:
            return [value for name, value in cls.__dict__.items() if name == key.upper()][0]
        except Exception:
            return None

    @classmethod
    def name(cls, key):
        try:
            return [name for name, value in cls.__dict__.items() if value == key][0]
        except Exception:
            return None

    @classmethod
    def get_counter(cls):
        counter = {}
        for key, value in cls.__dict__.items():
            if key.isupper():
                counter[value] = 0
        return counter

    @classmethod
    def items(cls):
        attrs = [a for a in cls.__dict__.keys() if a.isupper()]
        values = [(v, cls.__dict__[v]) for v in attrs]
        return sorted(values, key=lambda x: x[1])

    @classmethod
    def is_valid_transition(cls, from_status, to_status):
        return from_status == to_status or from_status in cls.transition_origins(to_status)

    @classmethod
    def transition_origins(cls, to_status):
        return cls._transitions[to_status]

    @classmethod
    def get_name(cls, key):
        choices_name = dict(cls.choices())
        return choices_name.get(key)


class UserTypes(CustomEnum):
    SUPERUSER = 0
    ADMIN = 1
    BLOGGER = 2
    USER = 3

    @classmethod
    def choices(cls):
        return (
            (cls.SUPERUSER, "Superuser"),
            (cls.ADMIN, "Admin"),
            (cls.BLOGGER, "Blogger"),
            (cls.USER, "User"),
        )


class SocialMediaTypes(CustomEnum):
    INSTAGRAM = 0
    FACEBOOK = 1
    TWITTER = 2
    YOUTUBE = 3

    @classmethod
    def choices(cls):
        return (
            (cls.INSTAGRAM, "Instagram"),
            (cls.FACEBOOK, "Facebook"),
            (cls.TWITTER, "Twitter"),
            (cls.YOUTUBE, "Youtube"),
        )


class SocialMediaUrls(CustomEnum):
    INSTAGRAM = 0
    FACEBOOK = 1
    TWITTER = 2
    YOUTUBE = 3

    @classmethod
    def choices(cls):
        return (
            (cls.INSTAGRAM, "https://instagram.com/"),
            (cls.FACEBOOK, "https://facebook.com/"),
            (cls.TWITTER, "https://twitter.com/"),
            (cls.YOUTUBE, "https://youtube.com/"),
        )


class SocialMediaIcons(CustomEnum):
    INSTAGRAM = 0
    FACEBOOK = 1
    TWITTER = 2
    YOUTUBE = 3

    @classmethod
    def choices(cls):
        return (
            (cls.INSTAGRAM, "fa fa-instagram"),
            (cls.FACEBOOK, "fa fa-facebook"),
            (cls.TWITTER, "fa fa-twitter"),
            (cls.YOUTUBE, "fa fa-youtube"),
        )


class Genders(CustomEnum):
    MALE = 0
    FEMALE = 1
    UNISEX = 2

    @classmethod
    def choices(cls):
        return (
            (cls.MALE, "Male"),
            (cls.FEMALE, "Female"),
            (cls.UNISEX, "Unisex"),
        )


class MediaTypes(CustomEnum):
    IMAGE = 0
    VIDEO = 1
    AUDIO = 2

    @classmethod
    def choices(cls):
        return (
            (cls.IMAGE, "Image"),
            (cls.VIDEO, "Video"),
            (cls.AUDIO, "Audio"),
        )
