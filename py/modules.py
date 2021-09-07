def shutdown(servers):
    """Verifies and shutdown any server which has 0 users."""
    server_id = len(servers) - 1
    while server_id >= 0:
        if servers[server_id].get_users() == 0:
            del servers[server_id]
        server_id -= 1
    return servers

def clean_users(users):
    """Decrements, verifies and clean each user which has completed their task."""
    user_id = len(users) - 1
    while user_id >= 0:
        users[user_id].decrement()
        if users[user_id].return_ticks() == 0:
            server = users[user_id].return_server()
            server.decrement()
            del users[user_id]
        user_id -= 1
    return users

def server_string(servers):
    """Go through all the servers and concatenate a string of its users."""
    fmt = ""
    for server in servers:
        fmt += str(server.get_users()) + ','
    return fmt[:-1] + '\n'
