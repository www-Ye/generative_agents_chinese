import os

proxy = ""
os.environ["http_proxy"] = proxy
os.environ["https_proxy"] = proxy

# Copy and paste your OpenAI API Key
openai_api_key = ""
# Put your name
key_owner = ""

maze_assets_loc = "../../environment/frontend_server/static_dirs/assets"
env_matrix = f"{maze_assets_loc}/the_ville/matrix"
env_visuals = f"{maze_assets_loc}/the_ville/visuals"

fs_storage = "../../environment/frontend_server/storage"
fs_temp_storage = "../../environment/frontend_server/temp_storage"

collision_block_id = "32125"

# Verbose 
debug = True