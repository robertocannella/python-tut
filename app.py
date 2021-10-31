people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson',
          'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']


def split_title_and_name(person):
    person.replace(person.split(' ')[1], '')
    return " ".join(person.split())


print(list(map(split_title_and_name, people)))
