"""Configuration for the LLM Council."""

import os
from dotenv import load_dotenv

load_dotenv()

# OpenRouter API key
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# OpenRouter API endpoint
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"

# Data directory for conversation storage
DATA_DIR = "data/conversations"

# -------------------------------------------------------------------
# To switch configs, set COUNCIL_CONFIG in your .env file:
#
#   COUNCIL_CONFIG=budget
#   COUNCIL_CONFIG=balanced   ← default if not set
#   COUNCIL_CONFIG=quality
# -------------------------------------------------------------------

_profile = os.getenv("COUNCIL_CONFIG", "balanced").lower().strip()

if _profile == "budget":
    from .config_budget import COUNCIL_MODELS, CHAIRMAN_MODEL
elif _profile == "quality":
    from .config_quality import COUNCIL_MODELS, CHAIRMAN_MODEL
else:
    from .config_balanced import COUNCIL_MODELS, CHAIRMAN_MODEL

# Print confirmation at startup so you always know which config is active.
print(f"[council] Active config: {_profile.upper()}")
print(f"[council] Council : {COUNCIL_MODELS}")
print(f"[council] Chairman: {CHAIRMAN_MODEL}")
