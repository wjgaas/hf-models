# Download a single file
# from huggingface_hub import hf_hub_download
# hf_hub_download(repo_id="tiiuae/falcon-7b-instruct", filename="config.json")

# Or an entire repository
from huggingface_hub import snapshot_download
# snapshot_download("JunhaoZhuang/PowerPaint-v1"
#                   )
# snapshot_download("SG161222/RealVisXL_V3.0"
#                   )
snapshot_download("stabilityai/sdxl-turbo",
                  allow_patterns=[
                    "model_index.json",
                    "scheduler/scheduler_config.json",
                    "text_encoder/config.json,
                    "text_encoder/model.fp16.safetensors",
                    "text_encoder_2/config.json,
                    "text_encoder_2/model.fp16.safetensors",
                    "tokenizer/",
                    "tokenizer_2/",
                    "unet/config.json",
                    "unet/diffusion_pytorch_model.fp16.safetensors",
                    "vae/config.json",
                    "vae/diffusion_pytorch_model.fp16.safetensors",
                  ]
                  )
# Download from a dataset
#from huggingface_hub import snapshot_download
# snapshot_download(repo_id="bigcode/starcoderdata", repo_type="dataset", allow_patterns=["git-commits-cleaned/train-00000-of-00055.parquet", "github-issues-filtered-structured/train-00000-of-00059.parquet"])
#snapshot_download(repo_id="playgroundai/playground-v2-1024px-aesthetic", repo_type="dataset")

# See more at https://huggingface.co/docs/huggingface_hub/en/guides/download
