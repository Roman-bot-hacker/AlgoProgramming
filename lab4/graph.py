class Graph:

    def __init__(self, graph):
        self._depth_level = 2
        self.depth_level_count = 0
        self.net_dict = graph
        self.friend_count_list = []
        self.most_active_student = None
        self.friend_set = set()

    def search_most_active_student(self):
        self.__width_search()
        return self.__get_most_active_student()

    def __width_search(self):
        for student in self.net_dict:
            self.friend_set.clear()
            self.__friend_search(self.net_dict[student], student)
            self.friend_count_list.append(len(self.friend_set))

    def __friend_search(self, student_friends_list, student):
        self.depth_level_count += 1
        for friend in student_friends_list:
            if friend == student:
                continue
            self.friend_set.add(friend)
            if self.depth_level_count < self._depth_level:
                self.__friend_search(self.net_dict[friend], student)
        self.depth_level_count -= 1

    def __get_most_active_student(self):
        for student in range(0, len(self.friend_count_list)):
            if self.most_active_student is None:
                self.most_active_student = student
            elif self.friend_count_list[student] > self.friend_count_list[self.most_active_student]:
                self.most_active_student = student
        return self.most_active_student.__str__()