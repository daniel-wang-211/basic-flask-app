from ast import Dict
from enum import Enum, EnumMeta
from itertools import chain
import logging
from typing import ClassVar, Optional, Tuple, Type
from typing_extensions import reveal_type

logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)

class MetaEnum(EnumMeta):
    def __contains__(cls, item):
        try:
            cls(item)  # type: ignore
        except ValueError:
            return False
        return True
module = __name__
member = MetaEnum
mms = dir(MetaEnum)
print(mms)

for class_member_name in mms:

    class_member = getattr(member, class_member_name)
    if type(class_member).__name__ == "function":
        name = f"{member.__name__}.{class_member.__name__}"
        print(name)
    else:
        print("else")




class CaseCompactStringEnum(str, Enum, metaclass=MetaEnum):
    @classmethod
    def _missing_(cls, value: str):
        for member in cls:
            if member.value.lower() == value.lower():
                return member

    def __str__(self) -> str:
        return self.value


class AuthHeaderKey(CaseCompactStringEnum):
    USER_ID = 'X-Xyz-User-Id'
    AUTH = 'X-Xyz-Auth'
    END_CLIENT = 'X-Xyz-End-Client'
    USER_AGENT = 'X-Forwarded-User-Agent'
    LOCKOUT = 'X-Xyz-Lockout'

from typing import TypeVar, Generic

# KT = TypeVar("KT")
# VT = TypeVar("VT")

# class RestrictStrDict(Mapping[KT, VT]):
#     def __init__(self, mapping=(), **kwargs):
#         self.data: Dict[KT, VT] = {}
#         logger.info("handle args")
#         aaa = self._process_args(mapping, **kwargs)
#         logger.info("init")
#         self.data.update(aaa)
#         # super().__init__(aaa)
#         logger.warning("__init__ done!!!")

#     def __getitem__(self, key: VT) -> Optional[VT]:
#         if key not in AuthHeaderKey:
#             return None
#         return self.data[key]
#         # return super().__getitem__(key)

#     def __setitem__(self, key: KT, val: VT):
#         if key not in AuthHeaderKey:
#             return None
#         self.data[key] = val
#         # super().__setitem__(key, val)

#     # def __init__(self, dictionary=None, /, **kwargs) -> None:
#     #     self.data: Dict[KT, VT] = {}
#     #     if dictionary is not None:
#     #         self.update(dictionary)
#     #     if kwargs:
#     #         self.update(kwargs)

#     def __contains__(self, key: KT) -> bool:
#         return key in self.data

#     def __delitem__(self, key: KT) -> None:
#         del self.data[key]

#     def __len__(self) -> int:
#         return len(self.data)

#     def __iter__(self) -> Iterator[KT]:
#         return iter(self.data)

#     @classmethod
#     def fromkeys(cls, iterable: Iterable[KT], value: VT) -> "MyDict":
#         """Create a new dictionary with keys from `iterable` and values set
#         to `value`.

#         Args:
#             iterable: A collection of keys.
#             value: The default value. All of the values refer to just a single
#                 instance, so it generally does not make sense for `value` to be a
#                 mutable object such as an empty list. To get distinct values, use
#                 a dict comprehension instead.

#         Returns:
#             A new instance of MyDict.
#         """
#         d = cls()
#         for key in iterable:
#             d[key] = value
#         return d



#     @staticmethod # because this doesn't make sense as a global function.
#     def _process_args(mapping=(), **kwargs) -> Iterator[Tuple[KT, VT]]:
#         logger.warning("Enter processing!!!     ")
#         if hasattr(mapping, "items"):
#             logger.info("has items. %s", mapping)
#             mapping = getattr(mapping, "items")()
#             logger.info("[%s]:%s",mapping, len(mapping))
#             logger.info("[%s]",mapping)
#         logger.info("kwargs, %s" %kwargs)
#         return ((KT(k), v) for k, v in chain(mapping, getattr(kwargs, "items")()) if k in KT)

#     def update(self, mapping=(), **kwargs):
#         logger.info("update called.")
#         self.data.update(self._process_args(mapping, **kwargs))

# class AuthHeader(Dict[AuthHeaderKey, str]):

#     def __init__(self, *args: Any, **kwargs: Any) -> None:
#         data = Dict(*args, **kwargs)
#         super().__init__()
#         self.update(data)

#     def update(self, mapping=(), **kwargs):
#         data = {}
#         data.update(mapping, **kwargs)
#         self._update(data)

#     def _update(self, data):
#         for k, v in data:
#             try:
#                 key = AuthHeaderKey(k)
#                 val = str(v)
#                 self.__setitem__(key, val)
#             except:
#                 pass

KT = TypeVar("KT", bound=Enum)

class RestrictDict(dict, Generic[KT]):
    enum: ClassVar[Type[KT]]

    def __init__(self, mapping=(), **kwargs):
        logger.info("handle args, %s", reveal_type(KT))
        aaa = self._process_args(mapping, **kwargs)
        logger.info("init")
        super().__init__(aaa)
        logger.warning("__init__ done!!!")

    def __getitem__(self, key: str) -> Optional[str]:
        if key not in self.enum:
            return None
        return super().__getitem__(key)

    def __setitem__(self, key: KT, val: str):
        if key not in self.enum:
            return None
        super().__setitem__(key, val)

    # # @classmethod # because this doesn't make sense as a global function.
    # def _process_args(self,  mapping=(), **kwargs):
    #     logger.warning("Enter processing!!!     ")
    #     if hasattr(mapping, "items"):
    #         logger.info("has items. %s", mapping)
    #         mapping = getattr(mapping, "items")()
    #         logger.info("[%s]:%s",mapping, len(mapping))
    #         logger.info("[%s]",mapping)
    #     logger.info("kwargs, %s" %kwargs)
    #     return ((self.enum(k), v) for k, v in chain(mapping, getattr(kwargs, "items")()) if k in self.enum)

    @classmethod # because this doesn't make sense as a global function.
    def _process_args(cls, mapping=(), **kwargs):
        if hasattr(mapping, "items"):
            mapping = getattr(mapping, "items")()
        return (
            (cls.enum(k), v)
            for k, v in chain(mapping, getattr(kwargs, "items")())
            if k in cls.enum
        )

    def update(self, mapping=(), **kwargs):
        logger.info("update called.")
        super().update(self._process_args(mapping, **kwargs))

class AuthHeader(RestrictDict[AuthHeaderKey]):
    enum = AuthHeaderKey


# class AuthHeader2(dict):

#     def __init__(self, mapping=(), **kwargs):
#         logger.info("handle args")
#         aaa = self._process_args(mapping, **kwargs)
#         logger.info("init")
#         super().__init__(aaa)
#         logger.warning("__init__ done!!!")

#     def __getitem__(self, key: str) -> Optional[str]:
#         if key not in AuthHeaderKey:
#             return None
#         return super().__getitem__(key)

#     def __setitem__(self, key: AuthHeaderKey, val: str):
#         if key not in AuthHeaderKey:
#             return None
#         super().__setitem__(key, val)

#     @staticmethod # because this doesn't make sense as a global function.
#     def _process_args(mapping=(), **kwargs):
#         logger.warning("Enter processing!!!     ")
#         if hasattr(mapping, "items"):
#             logger.info("has items. %s", mapping)
#             mapping = getattr(mapping, "items")()
#             logger.info("[%s]:%s",mapping, len(mapping))
#             logger.info("[%s]",mapping)
#         logger.info("kwargs, %s" %kwargs)
#         return ((AuthHeaderKey(k), v) for k, v in chain(mapping, getattr(kwargs, "items")()) if k in AuthHeaderKey)

#     def update(self, mapping=(), **kwargs):
#         logger.info("update called.")
#         super().update(self._process_args(mapping, **kwargs))


class TestEnumDict:

    def test_init(self):
        d = {
            AuthHeaderKey.AUTH: "123",
            AuthHeaderKey.USER_AGENT: "chrome",
            'X-Xyz-Lockout': 'lo'
        }
        logger.info("build header")
        header = AuthHeader(d)

        logger.info("compare header")
        assert d == header

        assert "X-Xyz-Auth" in AuthHeaderKey

    def test_init_skip_unexpected(self):
        d = {
            AuthHeaderKey.AUTH: "123",
            AuthHeaderKey.USER_AGENT: "chrome",
            'X-Xyz-Lockout': 'lo',
        }
        d2 = dict(d)
        d2["abc"] = "123"
        header = AuthHeader(d2)
        logger.info(header)

        assert d == header
        assert d != d2

    def test_init_ignore_case(self):
        d = {
            'X-XYZ-LOCKOUT': 'lo',
        }
        expect = {
            AuthHeaderKey.LOCKOUT: 'lo',
        }
        header = AuthHeader(d)

        assert expect == header