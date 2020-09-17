"""CP1404/CP5632 Practical -
Programming language
Test run
Xander Dino Caubat"""

from Practicals.prac06.programming_language import ProgrammingLanguage


def run_test():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    languages = [ruby, python, visual_basic]
    print(visual_basic)

    print("The dynamically languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


if __name__ == "__main__":
    run_test()
