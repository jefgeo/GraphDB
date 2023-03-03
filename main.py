from Node import *


def analyze_strengths():

    my_nodes = Nodes()
#todo:  create different node types for people vs strengths
    people_list = ['Aishwarya', 'Brandon', 'Jeff', 'Vindhya', 'Kankshi', 'Himanshu', 'Ronit', 'Snehith', 'Josh',
                   'Krissy', 'Chad']
    for person in people_list:
        my_nodes.add_node(Node(person))

    strengths_list = ['Achiever', 'Adaptability', 'Analytical', 'Arranger', 'Communication', 'Competition', 'Context',
                       'Deliberative', 'Discipline', 'Focus', 'Futuristic', 'Ideation', 'Individualization', 'Input',
                       'Intellection', 'Learner', 'Maximizer', 'Positivity', 'Relator', 'Responsibility',
                       'Restorative', 'Significance', 'Strategic']
    for strength in strengths_list:
        my_nodes.add_node(Node(strength))

    mapping = [
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

    print(mapping)
    for item in mapping:
        my_nodes.get_node_by_key(item[0]).add_relationship(my_nodes.get_node_by_key(item[1]))

    for strength in my_nodes:
        print(strength)

    print(my_nodes.get_node_by_key("Aishwarya").list_relationships())

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    analyze_strengths()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
