from dataclasses import dataclass

@dataclass(frozen=True)
class OsInfo:
    """Value Object to store OS Info"""
    id: str
    version_id: str
    name: str = ""
    pretty_name: str = ""
    version_codename: str = ""

    def __post_init__(self):
        """Check the existence of mandatory properties"""
        if not self.id or not self.version_id:
            raise ValueError("ID and VERSION_ID cannot be empty")
