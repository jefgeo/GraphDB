from Node import *


def analyze_strengths():

    my_nodes = Nodes()

    # Add People as nodes.
    people_list = ['Aishwarya', 'Brandon', 'Jeff', 'Vindhya', 'Kankshi', 'Himanshu', 'Ronit', 'Snehith', 'Josh',
                   'Krissy', 'Chad']
    for person in people_list:
        my_nodes.add_node(Node(person, 'Person'))

    # Add strengths as nodes.
    strengths_list = ['Achiever', 'Adaptability', 'Analytical', 'Arranger', 'Communication', 'Competition', 'Context',
                       'Deliberative', 'Discipline', 'Focus', 'Futuristic', 'Ideation', 'Individualization', 'Input',
                       'Intellection', 'Learner', 'Maximizer', 'Positivity', 'Relator', 'Responsibility',
                       'Restorative', 'Significance', 'Strategic']
    for strength in strengths_list:
        my_nodes.add_node(Node(strength, 'Strength'))

    # add Relationships
    relationships = [
        ['Aishwarya', 'Arranger'],
        ['Aishwarya', 'Positivity'],
        ['Aishwarya', 'Learner'],
        ['Aishwarya', 'Responsibility'],
        ['Aishwarya', 'Analytical'],
        ['Brandon', 'Ideation'],
        ['Brandon', 'Learner'],
        ['Brandon', 'Intellection'],
        ['Brandon', 'Futuristic'],
        ['Brandon', 'Relator'],
        ['Himanshu', 'Significance'],
        ['Himanshu', 'Futuristic'],
        ['Himanshu', 'Discipline'],
        ['Himanshu', 'Intellection'],
        ['Himanshu', 'Deliberative'],
        ['Kankshi', 'Input'],
        ['Kankshi', 'Analytical'],
        ['Kankshi', 'Achiever'],
        ['Kankshi', 'Individualization'],
        ['Kankshi', 'Competition'],
        ['Ronit', 'Maximizer'],
        ['Ronit', 'Analytical'],
        ['Ronit', 'Adaptability'],
        ['Ronit', 'Futuristic'],
        ['Ronit', 'Arranger'],
        ['Vindhya', 'Strategic'],
        ['Vindhya', 'Achiever'],
        ['Vindhya', 'Relator'],
        ['Vindhya', 'Discipline'],
        ['Vindhya', 'Learner'],
        ['Josh', 'Arranger'],
        ['Josh', 'Relator'],
        ['Josh', 'Restorative'],
        ['Josh', 'Responsibility'],
        ['Josh', 'Communication'],
        ['Krissy', 'Context'],
        ['Krissy', 'Achiever'],
        ['Krissy', 'Learner'],
        ['Krissy', 'Discipline'],
        ['Krissy', 'Relator'],
        ['Chad', 'Deliberative'],
        ['Chad', 'Analytical'],
        ['Chad', 'Focus'],
        ['Chad', 'Futuristic'],
        ['Chad', 'Intellection'],
        ['Snehith', 'Restorative'],
        ['Snehith', 'Responsibility'],
        ['Snehith', 'Analytical'],
        ['Snehith', 'Learner'],
        ['Snehith', 'Relator'],
        ['Jeff', 'Strategic'],
        ['Jeff', 'Individualization'],
        ['Jeff', 'Ideation'],
        ['Jeff', 'Relator'],
        ['Jeff', 'Intellection']
    ]

    # print(relationships)
    for item in relationships:
        my_nodes.get_node_by_key(item[0]).add_relationship(my_nodes.get_node_by_key(item[1]))


    for node in my_nodes:
        # Person
        if node.node_type == "Person":
            print('\n\n')
            linked_people = {}
            print(node)
            # Person's relationships (e.g. Strengths)
            for relationship in node.get_relationships_string():
                print(f'\t{relationship}')
                common_people_this_relationship = 0
                relationship_list = ''
                # Other people connected to that Node (e.g. those with same strengths)
                for relationship_2 in my_nodes.get_node_by_key(relationship).get_relationships_string():
                    if relationship_2 != node.key:
                        relationship_list += relationship_2 + ' '
                        if relationship_2 not in linked_people:
                            linked_people[relationship_2] = 1
                        else:
                            linked_people[relationship_2] += 1
                        common_people_this_relationship += 1
                if common_people_this_relationship == 0:
                    print(f'\t\t**Unique Trait for You**')
                else:
                    print(f'\t\tTotal of {common_people_this_relationship} others:  {relationship_list}')
            print('\n\tTotal Links')
            linked_people_sorted = sorted(linked_people.items(), key = lambda x: -x[1])
            for k,v in linked_people_sorted:
                print(f'\t\t{k}: {v}')


if __name__ == '__main__':
    analyze_strengths()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
