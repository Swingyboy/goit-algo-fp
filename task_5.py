import uuid
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from collections import deque

from typing import List, Optional, Literal

TREE_TYPE = Literal["binary", "heap"]
ALGORITHM = Literal["bfs", "dfs"]


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


def insert_to_heap(root: "Node", key: int) -> None:
    new_node = Node(key)
    queue = [root]
    while queue:
        temp = queue.pop(0)
        if not temp.left:
            temp.left = new_node
            return
        else:
            queue.append(temp.left)
        if not temp.right:
            temp.right = new_node
            return
        else:
            queue.append(temp.right)


def insert_to_binary_tree(root: "Node", key: int) -> "Node":
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert_to_binary_tree(root.left, key)
        else:
            root.right = insert_to_binary_tree(root.right, key)
    return root


def build_heap(elements: List[int], max_heap: bool = True) -> Node:
    if not elements:
        return None
    elements.sort(reverse=max_heap)
    root = Node(elements[0])
    for element in elements[1:]:
        insert_to_heap(root, element)
    return root


def build_binary_tree(elements: List[int]) -> Node:
    if not elements:
        return None
    average = sum(elements) / len(elements)
    root = min(elements, key=lambda x: abs(x - average))
    elements.remove(root)
    root = Node(root)
    for element in elements:
        insert_to_binary_tree(root, element)
    return root


def dfs(node: Node):
    if node is not None:
        stack = [(node, 0)]
        step = 0
        while stack:
            current, level = stack.pop()
            color = mcolors.to_hex(mcolors.hsv_to_rgb((0.46, 1.0, step / 6.0)))
            current.color = color

            step += 1
            if current.right:
                stack.append((current.right, level + 1))
            if current.left:
                stack.append((current.left, level + 1))


def bfs(node: Node):
    if node is not None:
        queue = deque([(node, 0)])
        step = 0
        while queue:
            current, level = queue.popleft()
            shade = min((step + 1) / 5.0, 1.0)
            color = mcolors.to_hex(mcolors.hsv_to_rgb((0.46, 1.0, shade)))
            current.color = color

            step += 1
            if current.left:
                queue.append((current.left, level + 1))
            if current.right:
                queue.append((current.right, level + 1))


def main(elements: List[int], algorithm: ALGORITHM = "bfs", tree_type: TREE_TYPE = "binary") -> None:
    if tree_type.lower() == "heap":
        root = build_heap(elements)
    elif tree_type.lower() == "binary":
        root = build_binary_tree(elements)
    else:
        raise ValueError(f"Invalid tree type {tree_type}")
    if algorithm.lower() == "bfs":
        bfs(root)
    elif algorithm.lower() == "dfs":
        dfs(root)
    draw_tree(root)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Draw a tree")
    parser.add_argument("elements", nargs="+", type=int, help="Elements to insert in the tree")
    parser.add_argument("--algorithm", type=str, default="bfs", help="Algorithm to use for coloring the tree")
    parser.add_argument("--tree-type", type=str, default="binary", help="Type of tree to build")
    args = parser.parse_args()
    main(args.elements, args.algorithm, args.tree_type)
