package main

type server struct {
  users, umax int
}

func NewServer(max int) *server {
  return &server{1, max}
}

func (s *server) add() {
  s.users++
}

func (s *server) dec() {
  s.users--
}

func (s *server) available() bool {
  if s.users < s.umax {
    return true
  }
  return false
}

func (s server) online() int {
  return s.users
}
