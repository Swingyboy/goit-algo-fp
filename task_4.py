import uuid
import networkx as nx
import matplotlib.pyplot as plt

from typing import List


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


def build_heap(elements: List[int], max_heap: bool = True) -> Node:
    if not elements:
        return None
    elements.sort(reverse=max_heap)
    root = Node(elements[0])
    for element in elements[1:]:
        insert_to_heap(root, element)
    return root


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Build a heap and draw it")
    parser.add_argument("--max_heap", action="store_true", help="Build a max heap")
    parser.add_argument("elements", nargs="+", type=int, help="Elements to build the heap")
    args = parser.parse_args()

    root = build_heap(args.elements, args.max_heap)
    draw_tree(root)

