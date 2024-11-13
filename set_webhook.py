import os
import requests
import argparse
from dotenv import load_dotenv

def setup_webhook(url=None):
    """Set up Telegram webhook"""
    load_dotenv()
    
    # Get environment variables
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    webhook_secret = os.getenv("WEBHOOK_SECRET")
    default_url = os.getenv("BOT_URL", "https://kitchenads.io/api/telegram")
    
    # Use provided URL or default
    webhook_url = url or default_url
    
    if not bot_token:
        print("❌ TELEGRAM_BOT_TOKEN not found in environment variables")
        return False
        
    print(f"\n🔄 Setting webhook URL: {webhook_url}")
    
    # Set webhook
    response = requests.post(
        f"https://api.telegram.org/bot{bot_token}/setWebhook",
        json={
            "url": webhook_url,
            "secret_token": webhook_secret,
            "allowed_updates": ["message", "callback_query"]
        }
    )
    
    if response.status_code == 200:
        print("✅ Webhook set successfully!")
        
        # Get webhook info
        info_response = requests.get(
            f"https://api.telegram.org/bot{bot_token}/getWebhookInfo"
        )
        
        if info_response.status_code == 200:
            info = info_response.json().get("result", {})
            print("\n📊 Webhook Status:")
            print(f"URL: {info.get('url')}")
            print(f"Custom certificate: {info.get('has_custom_certificate', False)}")
            print(f"Pending updates: {info.get('pending_update_count', 0)}")
            print(f"Last error: {info.get('last_error_message', 'None')}")
            return True
    
    print(f"❌ Failed to set webhook: {response.text}")
    return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Set up Telegram webhook')
    parser.add_argument('--url', help='Custom webhook URL (optional)')
    args = parser.parse_args()
    
    setup_webhook(args.url) 