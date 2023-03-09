from graph import *

'''
This is a more detailed report to show the power of linking the relationships
'''


def analyze_strengths():
    my_nodes = Nodes()

    # Add People as nodes.
    people_list = ['Aishwarya', 'Brandon', 'Chad', 'Himanshu', 'Jeff', 'Josh', 'Kankshi', 'Krissy', 'Ronit',
                   'Ruchita', 'Snehith', 'Vindhya']
    for person in people_list:
        my_nodes.add_node(Node(person, 'Person'))

    # Add strengths as nodes.
    strengths_list = ['Achiever', 'Adaptability', 'Analytical', 'Arranger', 'Communication', 'Competition',
                      'Connectedness', 'Context',
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
        ['Jeff', 'Intellection'],
        ['Ruchita', 'Restorative'],
        ['Ruchita', 'Connectedness'],
        ['Ruchita', 'Individualization'],
        ['Ruchita', 'Achiever'],
        ['Ruchita', 'Responsibility']
    ]


    for item in relationships:
        # my_nodes.get_node_by_key(item[0]).add_relationship(my_nodes.get_node_by_key(item[1]))
        my_nodes.add_relationship_by_key(item[0], item[1])

    for node in my_nodes:

        # Person
        if node.get_node_type() == "Person":
            linked_people = {}
            print(f'\n\n{node}')

            # Person's relationships (e.g. Strengths)
            common_people_total = 0
            out_string = ''
            for relationship in node.get_relationships():
                out_string += f'\n\t{relationship.get_key():18}'

                # Other people connected to that Node (e.g. those with same strengths)
                common_people_this_relationship = 0
                relationship_list = ''

                for relationship_2 in relationship.get_relationships():
                    if relationship_2.get_key() != node.get_key():
                        relationship_list += relationship_2.get_key() + ', '
                        if relationship_2.get_key() not in linked_people:
                            linked_people[relationship_2.get_key()] = 1
                        else:
                            linked_people[relationship_2.get_key()] += 1
                        common_people_this_relationship += 1
                if common_people_this_relationship == 0:
                    out_string += f'\t\t** Unique Trait for You **'
                else:
                    out_string += f'\t\t{common_people_this_relationship} others:  {relationship_list[:-2]}'
                common_people_total += common_people_this_relationship
            print(f'\t{out_string}')
            linked_people_sorted = sorted(linked_people.items(), key=lambda x: -x[1])
            print(f'\n\tTotal Links in Common: {common_people_total}')
            for k, v in linked_people_sorted:
                print(f'\t\t{k:10}\t{v}')



if __name__ == '__main__':
    analyze_strengths()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
