name = input("Enter Candidate Name: ")
qualification = input("Enter Qualification (B.Tech/M.Tech): ")
experience = int(input("Enter Years of Experience: "))
skills = input("Enter Skills: ")

if (qualification.lower() in ["b.tech", "m.tech"] and
    experience >= 2 and
    "python" in skills.lower()):
    print("\nCandidate Shortlisted")
else:
    print("\nCandidate Not Shortlisted")