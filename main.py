import bot
import database


if __name__ == '__main__':

    # insert database info into another file
    post = {"_id": 0, "name": "tim", "score": 5}
    database.collection.insert_one(post)
    # bot.run_discord_bot()

