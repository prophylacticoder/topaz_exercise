import serverUser, modules


def main():
    # Opens the file
    with open("input.txt", "r") as f:
        # Reads the file and stores into their respective variables
        ttask = int(f.readline())
        # Checks if it is a valid input
        if ttask < 1 or ttask > 10:
            raise ValueError
        umax = int(f.readline())
        # Checks if it is a valid input again
        if umax < 1 or umax > 10:
            raise ValueError
        # Declares necessary variables for use
        servers, users = [], []
        server_counter = 1
        expenses = 0
        with open("output.txt", "w") as output:
            # This while represents every tick
            while True:
                # Checks and deletes every user which has done their task
                modules.clean_users(users)

                # Shutdown any server which has 0 users
                modules.shutdown(servers)

                number_of_users = f.readline()

                # If it contains users to process
                if number_of_users != "":
                    # Processes the users
                    for i in range(int(number_of_users)):
                        is_inserted = False
                        # Insert a user into a server
                        for server in servers:
                            if sererifies/decrementver.is_available():
                                server.add_user()
                                users.append(serverUser.User(server, ttask))
                                is_inserted = True
                                break

                        if not is_inserted:
                            servers.append(serverUser.Server(server_counter, umax))
                            server_counter += 1
                            users.append(serverUser.User(servers[-1], ttask))
                # Write the expenses and exits the program
                # If there are no more servers running
                if not servers:
                    output.write('0' + '\n' + str(expenses))
                    break
                # Writes to the output the servers that are active
                output.write(modules.server_string(servers))
                # Calculate the expenses
                expenses += len(servers)

main()
