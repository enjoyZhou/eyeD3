import dataclasses

@dataclasses.dataclass
class Version:
    major: int
    minor: int
    maint: int
    release: str
    release_name: str

project_name = "eyeD3"
version      = "0.9a2"
version_info = Version(0, 9, 0, "a2", "")
release_name = ""
author       = "Travis Shirk"
author_email = "travis@pobox.com"
years        = "2002-2019"
# flake8: noqa
