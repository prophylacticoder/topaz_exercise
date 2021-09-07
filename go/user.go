package main

type user struct {
  ttask int
  s *server
}

func (u *user) dec() {
    u.ttask--
}

func (u user) ticks() int {
  return u.ttask
}
