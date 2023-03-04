class Node:
    """
    The Node is an entity in the graph.  It contains some metadata and can be linked
    to other Nodes using add_relationship.
    """
    def __init__(self, key, node_type=None, attributes=None) -> None:
        """
        Initialize the node
        :param key:  A description of the entity
        :param node_type: Optional organization of the entities (ie person vs strength)
        :param attributes: optional attributes (any data type)
        relationships is a list of pointers to other nodes.
        """
        self._key = key
        self._node_type = node_type
        self._attributes = attributes
        self._relationships = []

    def add_relationship(self, to_node) -> None:
        """
        Add a relationship from self, pointing to to_node
        :param to_node: The related Node
        :return: None
        """
        if to_node is not None:
            self._relationships.append(to_node)
        else:
            raise ValueError(f'to_node not found')

    def dump_node(self):
        """
        dump all data from the node.  Intended for debugging
        :return: A string with all data for the node.
        """
        return f'For node: {self._key} @ {hex(id(self))}' \
               f'\n\tnode_type={self._node_type}' \
               f'\n\tattributes={self._attributes}' \
               f'\n\trelationships={self._relationships}'

    def __str__(self):
        """
        Override string function to return the key
        """
        return f'{self._key}'

    def get_key(self):
        return self._key

    def get_node_type(self):
        return self._node_type

    def get_attributes(self):
        return self._attributes

    def get_relationships(self, return_node=True):
        """
        Returns a list of all relationships associated with the node.
        :param return_node: If true, the method returns a list of pointers to the nodes
                            If false, the method returns a list of keys
        :return:
        """
        relationship_list = []
        for relationship in self._relationships:
            if relationship != self._key:
                if return_node:
                    relationship_list.append(relationship)
                else:
                    relationship_list.append(relationship.get_key())
        return relationship_list


class Nodes:
    """
    a collection of Nodes.
    A simple list would work, but implementing as a class allows for more control and functionality.
    Need to update this at some point to deal with duplicates.
    """
    def __init__(self):
        self._nodes = []

    def add_node(self, node) -> None:
        """
        Add a node to the collection
        """
        self._nodes.append(node)

    def get_node_by_key(self, key):
        """
        search the collection of nodes based on the key value
        :return: a node with the given key.
        """
        for node in self._nodes:
            if node.get_key() == key:
                return node
        raise ValueError(f'Node with key \'{key}\' not found')

    def add_relationship_by_key(self, from_key, to_key):
        """
        Add a relationship between two nodes.
        node.add_relationship is called twice, once for each direction.
        """
        from_node = self.get_node_by_key(from_key)
        to_node = self.get_node_by_key(to_key)
        if to_node is not None and from_node is not None:
            from_node.add_relationship(to_node)
            to_node.add_relationship(from_node)
        else:
            raise ValueError(f'node not found')

    def __iter__(self):
        """
        called for iterator
        :return:
        """
        self.current_index = 0
        return self

    def __next__(self):
        """
        get next value for iterator
        """
        if self.current_index < len(self._nodes):
            self.current_index += 1
            return self._nodes[self.current_index - 1]
        raise StopIteration
