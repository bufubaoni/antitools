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
            node = Node(item.id, item.icon, None, list(), item.title, item.link)
            tree.append(node)
        else:
            node = Node(item.id, item.icon, item.parent, list(), item.title, item.link)
            nodeadd(node, tree)


def nodeadd(leaf, menu):
    for node in menu:
        if leaf.parent == node.id:
            node.leaf.append(leaf)
        else:
            nodeadd(leaf, node.leaf)


if __name__ == '__main__':
    menu = list()
    menu.append(Item(1, "icon", "", "title", "#"))
    menu.append(Item(2, "icon", 1, "title2", "#"))
    menu.append(Item(3, "icon", 2, "title3", "#"))
    menu.append(Item(4, "icon", 3, "title4", "#"))
    generator_menu(menu)

    print(tree)
