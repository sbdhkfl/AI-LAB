"""Metadata-only model registry."""
from dataclasses import dataclass
@dataclass(frozen=True)
class ModelInfo:
    name:str; family:str; license:str; local:bool=True; notes:str=""
DEFAULT_MODELS=[ModelInfo("llama-family","text-generation","varies",notes="Verify exact model license."),ModelInfo("mistral-family","text-generation","varies",notes="Verify exact model license."),ModelInfo("qwen-family","text-generation","varies",notes="Verify exact model license.")]
class ModelRegistry:
    def __init__(self,models=None): self.models=list(models or DEFAULT_MODELS)
    def list(self): return list(self.models)
    def find_family(self,family): return [m for m in self.models if m.family==family]
