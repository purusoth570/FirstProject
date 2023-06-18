

class timeallocation():
    def method_1(self):
        class_1 = {"10 AM": "true", "11 AM": "false", "12 PM": "false"}
        class_2 = {"10 AM": "false", "11 AM": "true", "12 PM": " false"}
        class_3 = {"10 AM": "false", "11 AM": "false", "12 PM": "true"}
        timelist = ["10 AM","11 AM", "12 PM"]
        users = 0
        while users<=1:
            a = input("enter the classroom:")
            b = input("enter the timing:")

            if b not in timelist:
                print("please enter a valid timeslot")
            elif a == "class_1":
                if class_1[b] == "true":
                    print("class_1 is assigned")
                    class_1[b] = "false"
                    users = users + 1
                else:
                     print("class_1 is not availble ")

            elif a == "class_2":
                if class_2[b] =="true":
                    print("class_2 is assigned")
                    class_2[b] = "false"
                else:
                    print("class_2 not available")  # users = users + 1
            elif a == "class_3":
                if class_3[b] == "true":
                    print("class_3 is assigned")
                    class_3[b] = "false"

                else:
                     print("class_3 not avaiable")  # users = users + 1
            else:
                print("class is already assigned")
obj = timeallocation()
obj.method_1()


