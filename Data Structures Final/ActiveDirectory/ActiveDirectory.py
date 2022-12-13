class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []
    
    def __repr__(self):
        return f'Group({self.name})'

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user in group.users:
        return True
    for group in group.groups:
        if user in group.users:
            return True
        else:
            if is_user_in_group(user, group):
                return True
    return False
    
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

parent_user = "parent_user"
sub_child_user = "sub_child_user"

sub_child.add_user(sub_child_user)
parent.add_user(parent_user)

child.add_group(sub_child)
parent.add_group(child)


groups = [parent, child, sub_child]
for group in groups:
    print(f'{group}: {group.groups}, {group.users}')
print('\n')
print(is_user_in_group('sub_child_user', child)) #--> Will return True because 'sub_child_user' is in 'subchild' group which is part of 'child' group.
print(is_user_in_group('parent_user', parent)) #--> Will return True because 'parent_user' is in 'parent' group.
print(is_user_in_group('parent_user', child)) #--> Will return False because 'parent_user' is not in 'child' group.