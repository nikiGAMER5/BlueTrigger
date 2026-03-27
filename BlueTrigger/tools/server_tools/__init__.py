from tools.server_tools.house_changer import run_house_changer
from tools.server_tools.theme_changer import run_theme_changer
from tools.server_tools.token_joiner import run_token_joiner
from tools.server_tools.token_leaver import run_token_leaver
from tools.server_tools.server_info import run_server_info
from tools.server_tools.token_nuker import run_token_nuker
from tools.server_tools.token_delete_friends import run_token_delete_friends
from tools.server_tools.token_block_friends import run_token_block_friends
from tools.server_tools.token_unblock_users import run_token_unblock_users
from tools.server_tools.token_spammer import run_token_spammer

SERVER_TOOLS = {
    11: run_house_changer,
    12: run_theme_changer,
    13: run_token_joiner,
    14: run_token_leaver,
    15: run_server_info,
    16: run_token_nuker,
    17: run_token_delete_friends,
    18: run_token_block_friends,
    19: run_token_unblock_users,
    20: run_token_spammer,
}