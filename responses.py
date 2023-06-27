
def get_response(message: str) -> str:
    str_message = message.lower()

    if str_message[0:7] == '/tattle':
        # delegating tattling to its own function
        # need a function to search the enemy db
        return 'this is a tattle message for the enemy you named'

    # need an if statement for more specified enemy data, if person doesn't want full info sheet every time

    if str_message == '!help':
        return '`This is a help message.`'
        # will need to pad out this statement to give a more detailed help message

    return 'I didn\'t understand what you wrote.'


def get_tattle(enemy: str) -> str:
    return ''