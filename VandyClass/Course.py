class Course: #why (object)? Test this later

    def init(self):
        self.subject = ""
        self.number = 0
        self.hours = 0
        self.prereq = "" #do a name-search to check for prereqs

def main():
    course = Course()
    action = input("Select new course ? [Y]/[N]")
    if action == 'Y':
        course.subject = input("Course subject: ")
        course.number = input("Course number: ")
        course.hours = input("Course hours: ")
        course.prereq = input("Prerequisites: ")
        print("You have selected {} {} which will eat up {} hours in your schedule. Hold your asses because you'll have to take {} first bitch.".format(course.subject, course.number, course.hours, course.prereq))
    elif action == 'N':
        print("lol k bye")
        quit()
    else:
        print ("stop stop i don't know how to deal with that")
        main()

main()