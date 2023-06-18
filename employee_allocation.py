
team_1 = {"person_1":25000,"person_2":30000,"person_3":40000,"person_4":75000,"person_5":100000}
team_2 = {"person_6":25000,"person_7":30000,"person_8":40000,"person_9":75000,"person_10":100000}
team_3 = {"person_11":25000,"person_12":30000,"person_13":40000,"person_14":75000,"person_15":100000}

team_1_sal = sum(team_1.values())
team_2_sal = sum(team_2.values())
team_3_sal = sum(team_3.values())

d = "yes"
a = input("enter the under performance team:")
while d == "yes":
    person = input("enter the person to move:")
    b = input("enter the team to move:")

    if a == "team_1":
        if b == "team_2":
            team_2.update({person:team_1[person]})
        else:
            team_3.update({person:team_1[person]})
        del team_1[person]


    elif a == "team_2":
        if b == "team_1":
            team_1.update({person:team_2[person]})
        else:
            team_3.update({person:team_2[person]})
        del team_2[person]


    elif a == "team_3":
        if b == "team_2":
            team_2.update({person:team_3[person]})
        else:
            team_1.update({person:team_3[person]})
        del team_3[person]

    else:
        print("please enter a valid team name")

    print("after changing person salaries of team\n")

    if team_1_sal == sum(team_1.values()):
        print("the salary of team_1 is not changed:",team_1_sal)
    else:
      print("salary of 1st team is becoz",person,"is changed from",a,"to",b,"so the salary of team_1 is",sum(team_1.values()))

    if team_2_sal == sum(team_2.values()):
        print("the salary of team_2 is not changed:",team_2_sal)
    else:
     print("salary of 2nd team,",person,"is changed from",a,"to",b,"so the salary of team_2 is",sum(team_2.values()))

    if team_3_sal == sum(team_3.values()):
        print("the salary of team_3 is not changed:",team_3_sal)
    else:
     print("salary of 3rd team",person,"is changed from",a,"to",b,"so the salary of team_3 is",sum(team_3.values()))


    e = input("Do you want to continue(yes/no):")

    if e == "yes":
        d = "yes"
    else:
        d = "no"
