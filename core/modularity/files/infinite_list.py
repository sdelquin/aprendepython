class InfiniteList:
    def __init__(self, *args, fill_value=None):
        self.items = []
        for item in args:
            self.items.append(item)
        self.fill_value = fill_value

    def __getitem__(self, index: int):
        return self.items[index]

    def __len__(self):
        return len(self.items)

    def __setitem__(self, index: int, item) -> None:
        for _ in range(len(self), index + 1):
            self.items.append(self.fill_value)
        self.items[index] = item

    def __str__(self):
        return ','.join(str(i) for i in self.items)
