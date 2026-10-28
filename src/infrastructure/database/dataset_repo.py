# Concrete implementation of dataset repository
import os
import csv
import shutil
from domain.interfaces.dataset_repository import DatasetRepositoryInterface
from config.settings import settings

class FileDatasetRepository(DatasetRepositoryInterface):
    def __init__(self, base_dataset_dir: str = "datasets"):
        self.base_dataset_dir = base_dataset_dir

    def export_sample(self, video_name: str, frame_id: str, label: str) -> str:
        # Ruta del frame cacheado
        source_path = os.path.join(settings.qdrant_storage_path, "frame_cache", video_name, f"{frame_id}.jpg")
        if not os.path.exists(source_path):
            raise FileNotFoundError(f"El fotograma origen no existe en caché: {video_name}/{frame_id}")

        # Directorio de la clase/etiqueta
        label_dir = os.path.join(self.base_dataset_dir, label)
        os.makedirs(label_dir, exist_ok=True)

        dest_filename = f"{video_name}_{frame_id}.jpg"
        dest_path = os.path.join(label_dir, dest_filename)

        # Copiar imagen
        shutil.copy(source_path, dest_path)

        # Registrar en metadata.csv global del dataset para trazabilidad masiva
        csv_path = os.path.join(self.base_dataset_dir, "metadata.csv")
        file_exists = os.path.exists(csv_path)
        
        with open(csv_path, mode="a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(["image_path", "video_name", "frame_id", "label"])
            writer.writerow([dest_path, video_name, frame_id, label])

        return dest_path
