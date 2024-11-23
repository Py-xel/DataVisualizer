from abc import abstractmethod
from ItemName import ItemName
from SectionItem import SectionItem


class Section:
    def __init__(self) -> None:
        self.items: dict[ItemName, SectionItem] = dict()

    def add_item(self, item_name: ItemName, item: SectionItem) -> None:
        self.items[item_name] = item

    @abstractmethod
    def proceed(self) -> None:
        pass

    def get_yes_no_options(self) -> dict[int, str]:
        return {1: "Yes", 2: "No"}

    def to_bold(self, options: dict[int, str]) -> dict[int, str]:
        result: dict[int, str] = dict()
        for k, v in options.items():
            result[k] = f"\033[1m{v}\033[0m"
        return result