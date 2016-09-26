#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2016/9/26
from collections import namedtuple

Item = namedtuple("Item", ["id", "icon", "parent", "title", "link"])

Node = namedtuple("Node", ["id", "icon", "parent", "leaf", "title", "link"])

tree = list()


def generator_menu(menu):
    for item in menu:
        if not item.parent:
            node = Node(item.id, item.icon, "", list(), item.title, item.link)
            tree.append(node)
        else:
            node = Node(item.id, item.icon, item.parent, list(), item.title, item.link)
            nodeadd(node, menu)


def nodeadd(leaf, menu):
    if leaf.parent in [node.id for node in tree]:
        for node in tree:
            if leaf.parent == node.id:
                node.leaf.append(leaf)
    else:
        item = filter(lambda x: x.id == leaf.parent, menu)[0]
        print(item)
        tree.append(Node(item.id, item.icon, item.parent, list(), item.title, item.link))
        tree[-1].leaf.append(leaf)


if __name__ == '__main__':
    menu = list()
    menu.append(Item(1, "icon", "", "title", "#"))
    menu.append(Item(2, "icon", 1, "title2", "#"))
    menu.append(Item(3, "icon", 1, "title3", "#"))
    menu.append(Item(4, "icon", 1, "title4", "#"))
    menu.append(Item(5, "icon", "", "title5", "#"))
    menu.append(Item(6, "icon", 5, "title6", "#"))
    menu.append(Item(7, "icon", 6, "title7", "#"))
    menu.append(Item(8, "icon", 5, "title8", "#"))
    menu.append(Item(9, "icon", 1, "title9", "#"))
    menu.append(Item(10, "icon", 1, "title10", "#"))
    generator_menu(menu)

    print(tree)
