import opencc


def s2t(words: str, wp: bool = True) -> str:
    converter = opencc.OpenCC("s2twp.json" if wp else "s2t.json")
    return converter.convert(words)


def main():
    running = True
    while running:
        print("Input content for converting. Input \"exit\" to exit.")
        words = input("> ")
        if words == "exit":
            running = False
        else:
            print(s2t(words))
            print(s2t(words, False))
            print()
    print("Exiting...")


if __name__ == "__main__":
    main()
