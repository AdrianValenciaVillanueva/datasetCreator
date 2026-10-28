# Domain models for dataset management
from dataclasses import dataclass

@dataclass
class DatasetExportResult:
    label: str
    saved_path: str
    total_images: int
