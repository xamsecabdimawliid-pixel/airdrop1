from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def website_button(url):
    keyboard = [
        [
            InlineKeyboardButton(
                "🌐 FUR WEBSITE-KA",
                url=url
            )
        ]
    ]

    return InlineKeyboardMarkup(keyboard)
