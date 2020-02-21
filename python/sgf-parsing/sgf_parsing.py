import re


class SgfTree:
    def __init__(self, properties=None, children=None):
        self.properties = properties or {}
        self.children = children or []

    def __eq__(self, other):
        if not isinstance(other, SgfTree):
            return False
        for k, v in self.properties.items():
            if k not in other.properties:
                return False
            if other.properties[k] != v:
                return False
        for k in other.properties.keys():
            if k not in self.properties:
                return False
        if len(self.children) != len(other.children):
            return False
        for a, b in zip(self.children, other.children):
            if a != b:
                return False
        return True

    def __ne__(self, other):
        return not self == other


def parse(input_string):
    node_regex = re.compile(r";(?:[A-Z]+(?:\[.*?\])+)+")
    input_string = input_string.replace("(", "", 1)  # Removing opening parentheses
    first_node = node_regex.search(input_string)
    if first_node is None:
        return None
    tree = parse_node(first_node[0])
    input_string = input_string[len(first_node[0]):]
    if input_string[0] == "(":
        children_regex = re.compile(r"(?:(?:\(.*\))+)([;|)]*)")
        children = children_regex.match(input_string)
        children = ["(" + child for child in children[0].split("(")][1:]
        for child in children:
            tree.children.append(parse(child))
    else:
        tree.children.append(parse(input_string))
    if None in tree.children:
        tree.children = []
    return tree


def parse_node(input_string):
    property_regex = re.compile(r"[A-Z]+(?:\[.*?\])+")
    properties = property_regex.findall(input_string)
    properties = [prop.split("[") for prop in properties]
    node = SgfTree()
    for prop in properties:
        node.properties[prop[0]] = [x[:-1] for x in prop[1:]]
    return node


treeeee = parse("(;FF[4](;B[aa];W[ab])(;B[dd];W[ee]))")
print(treeeee)
