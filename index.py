from package.modals.User import create_user, findOneUser
from package.modals.Project import createProject, findOneProject, deleteOneProject, findAllproject

while True:
    print('> Crowd Funding Application')
    print('> Registration - Press (1)')
    print('> Login - Press (2)')
    print('> Exit - Press (3)')

    userID = 0
    inputReader = int(input('> Your Choice: '))

    if inputReader == 1:
        while True:
            print('> ENTER YOUR DATA')
            firstName = input('> FirstName: ')
            lastName = input('> LastName:')
            email = input('> Email(please enter a valid email): ')
            password = input('> Password: ')
            confirmPassword = input('> Confirm Password: ')
            phoneNumber = input('> Phone Number (please enter a valid phone number): ')
            status = create_user(firstName, lastName, email, password, phoneNumber)
            if not status:
                print('> User Already Registered')
            else:
                print("> CONGRATULATION")
        break

    elif inputReader == 2:
        print('> USER LOGIN')
        while True:
            email = input('> email: ')
            password = input('> Password: ')
            userdata = findOneUser(email, password)
            print("result:", userdata)
            if not userdata:
                print('> Failed Login.')
            else:
                userID = userdata['_id']
                userFirstName = userdata['firstName']
                userLastName = userdata['lastName']
                userEmail = userdata['email']
                userPassword = userdata['password']
                userPhoneNumber = userdata['phoneNumber']

            while True:
                print('> Create Project - press (0)')
                print('> Delete Project - Press (1)')
                print('> View One Project - press (2)')
                print('> View All Projects - press (3)')
                print('> Exit - press (4)')
                userChoice = int(input('> your choice: '))

                if userChoice == 0:
                    userId = userID
                    title = input('> project title: ')
                    details = input('> project details: ')
                    total = int(input('> project total target: '))
                    startDate = input('> project start date: ')
                    endDate = input('> project end data: ')
                    projectStatus = createProject(userId, title, details, total, startDate, endDate)
                    if projectStatus:
                        print('> Project Created Successfully...')
                    else:
                        print('> Sorry Project Creation Failed...')

                elif userChoice == 1:
                    title = input('> enter project title: ')
                    status = deleteOneProject(userID, title)
                    if status:
                        print('> Project Deleted Successfully...')
                    else:
                        print('> Project Deletion Failed...')

                elif userChoice == 2:
                    title = input('> enter project title: ')
                    status = findOneProject(userID, title)
                    print(userID)
                    if status:
                        print(status)
                    else:
                        print(status)
                        print('> no matched project...')
                elif userChoice == 3:
                    print(findAllproject(userID))
                elif userChoice == 4:
                    break
                elif inputReader == 3:
                    break
    else:
        print('> Sorry, Enter Valid Input\n')
