from tools.misc_tools.token_mass_dm import run_token_mass_dm
from tools.misc_tools.token_delete_dm import run_token_delete_dm
from tools.misc_tools.id_to_token import run_id_to_token
from tools.misc_tools.snowflake_decoder import run_snowflake_decoder
from tools.misc_tools.bot_id_to_invite import run_bot_id_to_invite
from tools.misc_tools.webhook_info import run_webhook_info
from tools.misc_tools.webhook_generator import run_webhook_generator
from tools.misc_tools.webhook_spammer import run_webhook_spammer
from tools.misc_tools.webhook_deleter import run_webhook_deleter
from tools.misc_tools.nitro_generator import run_nitro_generator

MISC_TOOLS = {
    21: run_token_mass_dm,
    22: run_token_delete_dm,
    23: run_id_to_token,
    24: run_snowflake_decoder,
    25: run_bot_id_to_invite,
    26: run_webhook_info,
    27: run_webhook_generator,
    28: run_webhook_spammer,
    29: run_webhook_deleter,
    30: run_nitro_generator,
}