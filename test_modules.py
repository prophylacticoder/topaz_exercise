import unittest
import modules
import serverUser

class TestShutdown(unittest.TestCase):
    def test_shutdown(self):
        """Testing of the function shutdown()"""
        servers = []
        for server in range(10):
            servers.append(serverUser.Server(server, 10))
            servers[server].decrement()

        self.assertEqual(modules.shutdown(servers), [])

class TestCleanUser(unittest.TestCase):
    def test_clean_users(self):
        """Testing clean_users funcion."""
        servers, users = [], []
        counter = 1
        for user in range(5):
            is_inserted = False
            for server in servers:
                if server.is_available():
                    server.add_user()
                    users.append(serverUser.User(server, 5))
                    is_inserted = True
                    break
            if not is_inserted:
                servers.append(serverUser.Server(counter, 2))
                users.append(serverUser.User(servers[-1], 5))

        modules.clean_users(users)

        for user in users:
            self.assertEqual(user.return_ticks(), 4)


class TestServerString(unittest.TestCase):
    def test_server_string(self):
        """Testing server_string() func which returns a string."""
        servers = []
        for server in range(5):
            servers.append(serverUser.Server(server, 10))

        self.assertEqual(modules.server_string(servers), "1,1,1,1,1\n")

if __name__ == "__main__":
    unittest.main()
