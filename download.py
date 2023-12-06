# Download a single file
# from huggingface_hub import hf_hub_download
# hf_hub_download(repo_id="tiiuae/falcon-7b-instruct", filename="config.json")

# Or an entire repository
from huggingface_hub import snapshot_download
snapshot_download("playgroundai/playground-v2-1024px-aesthetic", ignore_patterns=["diffusion_pytorch_model.safetensors","diffusion_pytorch_model.bin","diffusion_pytorch_model.fp16.bin","model.safetensors","pytorch_model.fp16.bin","pytorch_model.bin"])

# Download from a dataset
#from huggingface_hub import snapshot_download
# snapshot_download(repo_id="bigcode/starcoderdata", repo_type="dataset", allow_patterns=["git-commits-cleaned/train-00000-of-00055.parquet", "github-issues-filtered-structured/train-00000-of-00059.parquet"])
#snapshot_download(repo_id="playgroundai/playground-v2-1024px-aesthetic", repo_type="dataset")

# See more at https://huggingface.co/docs/huggingface_hub/en/guides/download
