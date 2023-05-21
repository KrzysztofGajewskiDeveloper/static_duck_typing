## Structural subtyping (Static Duck Typing) with Protocols

This code showcases the concept of static duck typing in Python, utilizing the Protocol class from the typing module. Static duck typing is a mechanism that enforces type compatibility based on object structure and behavior, rather than relying on explicit type inheritance.

### Example Usage

The provided code demonstrates the usage of Protocols and static duck typing. It includes the definition of the Parent Protocol, which requires the presence of the children attribute and the raise_child method. The AdoptiveParent and BiologicalParent classes conform to this Protocol by implementing the necessary attributes and methods. These classes act as subtypes of the Parent Protocol, despite not explicitly inheriting from the Parent class.

By leveraging static duck typing and the Parent Protocol, the code exemplifies how the teach_values function can iterate over a list of parents and invoke the raise_child method on each parent. This demonstrates polymorphic behavior based on the structural compatibility of objects with the Parent Protocol.


```python

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
