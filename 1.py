from telegram.ext import Application, MessageHandler, filters
import os

TOKEN = "7660968231:AAE_zU2W0XBquoyrO22VtADv2s987v16OrM"

async def handler(update, context):
    chat = update.effective_chat
    if chat.type == "channel" and update.channel_post:
        user = update.channel_post.from_user

        users_file = "channel_users.txt"
        admins_file = "channel_admins.txt"

        # ذخیره‌ی کاربر در فایل متنی
        if user:
            name = f"{user.first_name or ''} {user.last_name or ''}".strip()
            username = f"@{user.username}" if user.username else ""
            line = f"{name} {username}\n"

            # فقط اگه قبلاً نوشته نشده
            if not os.path.exists(users_file) or line not in open(users_file, encoding="utf-8").readlines():
                with open(users_file, "a", encoding="utf-8") as f:
                    f.write(line)

        # ذخیره‌ی لیست ادمین‌ها در فایل جداگانه
        try:
            admins = await context.bot.get_chat_administrators(chat.id)
            with open(admins_file, "w", encoding="utf-8") as f:
                for admin in admins:
                    u = admin.user
                    name = f"{u.first_name or ''} {u.last_name or ''}".strip()
                    username = f"@{u.username}" if u.username else ""
                    f.write(f"{name} {username} ({u.id})\n")
        except Exception as e:
            print("خطا در گرفتن ادمین‌ها:", e)

        await context.bot.send_message(chat_id=chat.id, text="✅ اطلاعات ثبت شد")
    elif update.message:
        await update.message.reply_text("❌ این دستور فقط در چنل کار می‌کند.")

app = Application.builder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.ALL, handler))
app.run_polling()