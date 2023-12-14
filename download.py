# Download a single file
# from huggingface_hub import hf_hub_download
# hf_hub_download(repo_id="tiiuae/falcon-7b-instruct", filename="config.json")

# Or an entire repository
from huggingface_hub import snapshot_download
snapshot_download("SG161222/Realistic_Vision_V4.0_noVAE"
                  )
# Download from a dataset
#from huggingface_hub import snapshot_download
# snapshot_download(repo_id="bigcode/starcoderdata", repo_type="dataset", allow_patterns=["git-commits-cleaned/train-00000-of-00055.parquet", "github-issues-filtered-structured/train-00000-of-00059.parquet"])
#snapshot_download(repo_id="playgroundai/playground-v2-1024px-aesthetic", repo_type="dataset")

# See more at https://huggingface.co/docs/huggingface_hub/en/guides/download
