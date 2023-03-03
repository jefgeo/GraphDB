class Node:
    def __init__(self, key, node_type=None):
        self.key = key
        self.node_type = node_type
        self.attributes = {}
        self.relationships = []

    def add_relationship(self, to_node):
        if to_node is not None:
            self.relationships.append(to_node)
        else:
            raise ValueError(f'to_node not found')

    def __str__(self):
        return f'For node: {self.key} @ {hex(id(self))}' \
               f'\n\tnode_type={self.node_type}' \
               f'\n\tattributes={self.attributes}' \
               f'\n\trelationships={self.relationships}'

    def list_relationships(self):
        relationship_list = []
        for relationship in self.relationships:
            relationship_list.append(relationship.key)
        return relationship_list

class Nodes:

    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)

    def get_node_by_key(self, key):
        for node in self.nodes:
            if node.key == key:
                return node
        raise ValueError(f'Node with key \'{key}\' not found')

    def __iter__(self):
        self.current_index = 0
        return self

    def __next__(self):
        if self.current_index < len(self.nodes):
            self.current_index += 1
            return self.nodes[self.current_index - 1]
        raise StopIteration
