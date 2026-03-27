from tools.token_tools.token_info import run_token_info
from tools.token_tools.token_login import run_token_login
from tools.token_tools.token_onliner import run_token_onliner
from tools.token_tools.token_generator import run_token_generator
from tools.token_tools.token_disabler import run_token_disabler
from tools.token_tools.token_bio_changer import run_token_bio_changer
from tools.token_tools.token_alias_changer import run_token_alias_changer
from tools.token_tools.token_cstatus_changer import run_token_cstatus_changer
from tools.token_tools.token_pfp_changer import run_token_pfp_changer
from tools.token_tools.token_language_changer import run_token_language_changer

# Tool mapping
TOKEN_TOOLS = {
    1: run_token_info,
    2: run_token_login,
    3: run_token_onliner,
    4: run_token_generator,
    5: run_token_disabler,
    6: run_token_bio_changer,
    7: run_token_alias_changer,
    8: run_token_cstatus_changer,
    9: run_token_pfp_changer,
    10: run_token_language_changer,
}