from tools.new_tools.phone_lookup import run_phone_lookup
from tools.new_tools.email_lookup import run_email_lookup
from tools.new_tools.email_spammer import run_email_spammer
from tools.new_tools.ip_lookup import run_ip_lookup
from tools.new_tools.username_checker import run_username_checker
from tools.new_tools.discord_lookup import run_discord_lookup
from tools.new_tools.instagram_lookup import run_instagram_lookup
from tools.new_tools.twitter_lookup import run_twitter_lookup
from tools.new_tools.github_lookup import run_github_lookup
from tools.new_tools.reddit_lookup import run_reddit_lookup
from tools.new_tools.facebook_lookup import run_facebook_lookup
from tools.new_tools.tiktok_lookup import run_tiktok_lookup
from tools.new_tools.youtube_lookup import run_youtube_lookup
from tools.new_tools.snapchat_lookup import run_snapchat_lookup
from tools.new_tools.telegram_lookup import run_telegram_lookup

NEW_TOOLS = {
    31: run_phone_lookup,
    32: run_email_lookup,
    33: run_email_spammer,
    34: run_ip_lookup,
    35: run_username_checker,
    36: run_discord_lookup,
    37: run_instagram_lookup,
    38: run_twitter_lookup,
    39: run_github_lookup,
    40: run_reddit_lookup,
    41: run_facebook_lookup,
    42: run_tiktok_lookup,
    43: run_youtube_lookup,
    44: run_snapchat_lookup,
    45: run_telegram_lookup,
}