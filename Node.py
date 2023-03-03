class Node:
    def __init__(self, key, node_type=None):
        self._key = key
        self._node_type = node_type
        self._attributes = {}
        self._relationships = []

    def add_relationship(self, to_node):
        if to_node is not None:
            self._relationships.append(to_node)
        else:
            raise ValueError(f'to_node not found')

    def dump_node(self):
        return f'For node: {self._key} @ {hex(id(self))}' \
               f'\n\tnode_type={self._node_type}' \
               f'\n\tattributes={self._attributes}' \
               f'\n\trelationships={self._relationships}'

    def __str__(self):
        return f'{self._key}'

    def get_key(self):
        return self._key

    def get_node_type(self):
        return self._node_type

    def get_relationships(self, return_node=True):
        relationship_list = []
        for relationship in self._relationships:
            if relationship != self._key:
                if return_node:
                    relationship_list.append(relationship)
                else:
                    relationship_list.append(relationship.get_key())
        return relationship_list


class Nodes:

    def __init__(self):
        self._nodes = []

    def add_node(self, node):
        self._nodes.append(node)

    def get_node_by_key(self, key):
        for node in self._nodes:
            if node.get_key() == key:
                return node
        raise ValueError(f'Node with key \'{key}\' not found')

    def add_relationship_by_key(self, from_key, to_key):
        from_node = self.get_node_by_key(from_key)
        to_node = self.get_node_by_key(to_key)
        if to_node is not None and from_node is not None:
            from_node.add_relationship(to_node)
            to_node.add_relationship(from_node)
        else:
            raise ValueError(f'node not found')

    def __iter__(self):
        self.current_index = 0
        return self

    def __next__(self):
        if self.current_index < len(self._nodes):
            self.current_index += 1
            return self._nodes[self.current_index - 1]
        raise StopIteration
