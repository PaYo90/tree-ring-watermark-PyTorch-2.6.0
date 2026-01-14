"""
Monkey patch to fix compatibility between diffusers 0.11.1 and newer huggingface_hub

Problem: diffusers 0.11.1 imports cached_download from huggingface_hub,
but cached_download was removed in huggingface_hub >= 0.26.0 (replaced by hf_hub_download)

Solution: Add cached_download as an alias to hf_hub_download before diffusers tries to import it

Author: Szymon Zachariasz
"""

# Import hf_hub_download first
from huggingface_hub import hf_hub_download
import huggingface_hub

# Monkey patch: Add cached_download as an alias to hf_hub_download
# This must be done BEFORE diffusers tries to import cached_download
if not hasattr(huggingface_hub, 'cached_download'):
    huggingface_hub.cached_download = hf_hub_download
    print("[FIX] Added cached_download alias to huggingface_hub")
else:
    print("[FIX] cached_download already exists in huggingface_hub")
