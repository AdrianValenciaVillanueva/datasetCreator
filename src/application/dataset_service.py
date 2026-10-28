# Application service for dataset export
import os
import shutil
from domain.interfaces.dataset_repository import DatasetRepositoryInterface
from config.settings import settings

class DatasetService:
    def __init__(self, repository: DatasetRepositoryInterface):
        self.repository = repository

    def export_sample(self, video_name: str, frame_id: str, label: str) -> dict:
        if not video_name or not frame_id or not label:
            raise ValueError("video_name, frame_id y label no pueden estar vacíos")
        
        saved_path = self.repository.export_sample(video_name, frame_id, label)
        return {
            "status": "success",
            "label": label,
            "saved_path": saved_path
        }
