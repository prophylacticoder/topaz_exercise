package main

import (
  "os"
  "strconv"
  "log"
  "bufio"
  "io"
)

func parseFile(filename string) (int, int, []int) {
  // Function responsible for parsing the filename and returning
  // their respective variables
  f, err := os.Open(filename)
  if err != nil {
    log.Fatal("Err opening the file.")
  }
  defer f.Close()

  r := bufio.NewReader(f)

  l, err := r.ReadString('\n')
  ttask, _ := strconv.Atoi(l[:len(l)-1])
  l, err = r.ReadString('\n')
  umax, _ := strconv.Atoi(l[:len(l)-1])
  var xi []int
  for {
    l, err = r.ReadString('\n')
    if err == io.EOF {
      break
    }
    n, _ := strconv.Atoi(l[:len(l)-1])
    xi = append(xi, n)
  }
  return ttask, umax, xi
}

func insertUser(u int, xlu []user, svs []*server) ([]user, []*server) {
  for i := 1; i <= u; i++ {
    flag := false
    // Checks if there is any server available
    for _, s := range svs {
      // If there is a slot available, use it
      if s.available() {
        // Add a new user
        xlu = append(xlu, user{ttask, s})
        s.add()
        flag = true
        break
      }
    }
    if !flag {
      // Allocates a new server
      s := NewServer(umax)
      svs = append(svs, s)
      // Insert a new user into the new server
      xlu = append(xlu, user{ttask, s})
    }
  }

  return xlu, svs
}

func updateUsers(u []user) []user {
  l := len(u) - 1
  // Iterates over the user's object
  for ; l >= 0; l-- {
    // Decrement the ticks
    u[l].dec()
    // If the user has completed its task ticks == 0, then remove them
    if u[l].ticks() == 0 {
      u[l].s.dec()
      u = append(u[:l], u[l+1:]...)
    }
  }
  return u
}

func shutdown(s []*server) []*server {
  l := len(s) - 1
  for ; l >= 0; l-- {
    if s[l].online() == 0 {
      s = append(s[:l], s[l+1:]...)
    }
  }
  return s
}

func save(fileName, data string) {
  f, err := os.Create("output.txt")
  if err != nil {
    log.Fatal("Err writing to the file.")
  }
  defer f.Close()

  f.WriteString(data)
}
