from typing import Protocol, runtime_checkable
from dataclasses import dataclass, field


@dataclass
class Child:
    name: str
    ethics: list[str] = field(default_factory=list)

    def learn(self, values: str) -> None:
        self.ethics.append(values)


@runtime_checkable
class Parent(Protocol):
    children: list[Child]

    def raise_child(self, child: Child, values: str) -> None:
        ...


@dataclass
class AdoptiveParent:
    children: list[Child]

    def raise_child(self, child: Child, values: str) -> None:
        if child in self.children:
            lesson: str = f'remember to {values}'
            child.learn(lesson)

    def adopt(self, child: Child) -> None:
        self.children.append(child)


@dataclass
class BiologicalParent:
    children: list[Child]

    def raise_child(self, child: Child, values: str) -> None:
        if child in self.children:
            child.learn(values)


def teach_values(parent: Parent, value: str) -> None:
    for child in parent.children:
        parent.raise_child(child, value)


def main() -> None:
    john = AdoptiveParent([Child('Mike'), Child('Oskar')])
    monica = BiologicalParent([Child('Ann')])
    sofia = BiologicalParent([Child('John'), Child('Oliver')])

    ann: Child = monica.children[0]
    john.adopt(ann)

    parents: list[Parent] = [john, monica, sofia]

    value: str = 'be nice'
    for parent in parents:
        teach_values(parent, value)


if __name__ == '__main__':
    main()
