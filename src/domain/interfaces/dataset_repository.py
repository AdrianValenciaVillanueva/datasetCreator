# Abstract interface for dataset export repository
from abc import ABC, abstractmethod

class DatasetRepositoryInterface(ABC):

    @abstractmethod
    def export_sample(self, video_name: str, frame_id: str, label: str) -> str:
        """Exporta un fotograma al dataset de la etiqueta especificada."""
        pass
