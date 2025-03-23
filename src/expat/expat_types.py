from pydantic import BeforeValidator, SecretStr

from os.path import expandvars
from typing import Annotated


ExpandableString = Annotated[str, BeforeValidator(lambda s: expandvars(s))]
ExpandableSecretString = Annotated[SecretStr, BeforeValidator(lambda s: expandvars(s))]
ExpandableInt = Annotated[int, BeforeValidator(lambda s: int(expandvars(s)) if isinstance(s, str) else s)]
