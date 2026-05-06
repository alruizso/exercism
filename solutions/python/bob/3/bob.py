responses = {
    "question": "Sure.",
    "yell": "Whoa, chill out!",
    "yellq": "Calm down, I know what I'm doing!",
    "silence": "Fine. Be that way!",
    "else": "Whatever."
}

def response(hey_bob:str) -> str:
    question = True if hey_bob.strip().endswith("?") else False
    yell = True if hey_bob.isupper() else False
    yellq = True if question and yell else False
    silence = False if hey_bob.strip() else True

    if yellq:
        return responses["yellq"]
    if question:
        return responses["question"]
    if yell:
        return responses["yell"]
    if silence:
        return responses["silence"]
    return responses["else"]
