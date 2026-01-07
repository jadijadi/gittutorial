
from typing import Final


LINE_LENGTH: Final[int] = 50
SEPARATOR: Final[str] = "─" * LINE_LENGTH


def geek(title: str, message: str) -> None:

    formatted_title = title.center(LINE_LENGTH)

    output = (
        f"{SEPARATOR}\n"
        f"{formatted_title}\n"
        f"{SEPARATOR}\n"
        f"{message}\n"
    )

    print(output)

    
def main() -> None:

    geek(
        title="جادی",
        message="جادی، در دفاع از کیبور کبیر"
    )

    geek(
        title="آزادی",
        message="لعنت بر سانسورچی"
    )

    
if __name__ == "__main__":
    main()
