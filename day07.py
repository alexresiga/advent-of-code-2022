from dataclasses import dataclass, field
from typing import Optional


@dataclass
class File:
    name: str
    parent: Optional['File']
    is_dir: bool = False
    size: int = 0
    children: list['File'] = field(default_factory=list)

    def change_dir(self, dir_name):
        return next(c for c in self.children if c.name == dir_name)

    def get_size(self):
        return sum(c.get_size() for c in self.children) if self.is_dir else self.size


commands = [x.strip() for x in open('data.in').readlines()]
home = File('/', None, True)
current_dir = home
for line in commands:
    match line.split():
        case '$', 'cd', '/':
            current_dir = home
        case '$', 'cd', '..':
            current_dir = current_dir.parent
        case '$', 'cd', name:
            current_dir = current_dir.change_dir(name)
        case '$', 'ls':
            pass
        case 'dir', name:
            current_dir.children.append(File(name, current_dir, True))
        case size, name:
            current_dir.children.append(File(name, current_dir, False, int(size)))


def part1(start, res):
    for c in start.children:
        if c.is_dir:
            res = part1(c, res) + (c.get_size() if c.get_size() <= 100000 else 0)
    return res


def part2(start, t, res):
    for c in start.children:
        if c.is_dir:
            if c.get_size() >= t:
                res += part2(c, t, res) + [c.get_size()]
    return res


print(part1(home, 0))
target = 30000000 - (70000000 - home.get_size())
print(min(part2(home, target, [])))
