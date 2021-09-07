package main

import (
  "strconv"
)

var ttask, umax int

func main() {
  var nUsers []int
  ttask, umax, nUsers = parseFile("input.txt")

  var servers []*server
  var users []user
  var e int
  var opt string
  for {
    // Decrement and remove the users who have completed their task
    users = updateUsers(users)
    // Shutdowns any server which has less than 1 client
    servers = shutdown(servers)
    if nUsers != nil {
      // Insert users
      users, servers = insertUser(nUsers[0], users, servers)

      // Prepare new users to be used again
      if len(nUsers) > 1 {
        nUsers = nUsers[1:]
      } else {
        nUsers = nil
      }
    }
    // Update the expenses
    e += len(servers)

    for i := range servers {
      opt += strconv.Itoa(servers[i].online()) + ","
    }
    opt = opt[:len(opt)-1] + "\n"
    // If there is no more servers running, we are done.
    if len(servers) < 1 {
      opt += "0\n" + strconv.Itoa(e)
      break
    }
  }
  save("output.txt", opt)
}
