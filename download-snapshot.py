from huggingface_hub import snapshot_download

path = snapshot_download(
    repo_id="matnowa3/btc-ml-lstm",
    repo_type="dataset",
    local_dir="./data",
    local_dir_use_symlinks=False
)
