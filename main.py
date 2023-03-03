from Node import *


def analyze_strengths():

    my_nodes = Nodes()

    people_list = ['Aishwarya', 'Brandon', 'Jeff']
    # people_list = ['Aishwarya', 'Brandon', 'Jeff', 'Vindhya', 'Kankshi', 'Himanshu', 'Ronit', 'Snehith', 'Josh',
    #                'Krissy', 'Chad']
    for person in people_list:
        my_nodes.add_node(Node(person))

    strengths_list = ['Achiever', 'Adaptability', 'Analytical', 'Arranger', 'Communication']
    # strengths_list = ['Achiever', 'Adaptability', 'Analytical', 'Arranger', 'Communication', 'Competition', 'Context',
    #                   'Deliberative', 'Discipline', 'Focus', 'Futuristic', 'Ideation', 'Individualization', 'Input',
    #                   'Intellection', 'Learner', 'Maximizer', 'Positivity', 'Relator', 'Responsibility',
    #                   'Restorative', 'Significance', 'Strategic']
    for strength in strengths_list:
        my_nodes.add_node(Node(strength))

    mapping = {
        'Aishwarya' : 'Arranger'
    }

    # print(mapping)
    for k,v in mapping.items():
        my_nodes.get_node_by_key(k).add_relationship(my_nodes.get_node_by_key(v))

    for strength in my_nodes:
        print(strength)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    analyze_strengths()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
