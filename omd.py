def step2_umbrella():
    answer_umb = "\n\
        Утка добралась до места, не намокнув.\n\
        Она поставила сушиться зонт в центр бара\n\
        и поэтому все другие посетители на нее ругались.\n\
        Но утка была уверена - все просто завидуют ее красивому зонтику"
    return answer_umb


def step2_no_umbrella():
    answer_noumb = "\n\
    Утка добралась до места, но намокла.\n\
    'Хорошо, что бар в аквапарке и тут все мокрые. А то было бы неловко',\n\
    - подумала она"
    return answer_noumb


def step1():
    print("Утка-маляр 🦆 решила выпить зайти в бар. " "Взять ей зонтик? ☂️")
    option = ""
    options = {"да": True, "нет": False}
    while option not in options:
        print("Выберите: {}/{}".format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


if __name__ == "__main__":
    print(step1())
