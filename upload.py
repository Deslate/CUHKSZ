# export IGEM_USERNAME=YHW_CUHKSZ
# export IGEM_PASSWORD=614864Des

# pip install igem-wikisync

import igem_wikisync as sync

sync.run(
    team='CUHKSZ',
    src_dir='.',      # folder where your wiki is stored
    build_dir='./.wikisync_temp'     # folder where WikiSync will temporarily store your wiki before uploading
)

# python upload.py
