data = []


def clear():
    data.clear()


def empty():
    return len(data) == 0


def push(item):
    data.insert(0, item)


def pop():
    if empty():
        return None
    return data.pop(0)


def peek():
    if empty():
        return None
    return data[0]