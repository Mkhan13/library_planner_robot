# Classical Planning: Autonomous Library Book Retrieval Robot

## Part 1: Domain Selection & Description

### Real-World Scenario Being Modeled

This project models a real-world robot that operates inside a library. The robot's job is to retrieve the specified book from the library shelf and deliver it to the front desk for pick up.  

### Entities / Objects in the Domain

- The robot
- Books
- Locations:
  - `base:` the robot’s starting location
  - `shelf:` where the books are
  - `desk:` where the books get delivered

### Agent Objective

The robot’s goal is to retrieve a specific book from its shelf location and place it on the front desk. To accomplish this, the robot must navigate between locations, pick up the book, and deliver it to the desk for pick up.

### Why Planning Is Needed

This task cannot be solved by a simple reflex agent because the robot needs to make decisions and account for future outcomes in its decision making. A reflex agent that reacts only to the current state would fail to coordinate the many steps it needs to take to achieve the goal.

---

## Part 2: STRIPS Formalization

### Predicates / Fluents

`At(robot, location)`: The robot location
`At(book, location)`: The book(s) location
`Holding(book)`: The robot is holding a book
`HandEmpty`: The robot is not holding a book

---

### Action Schemas

#### Action: Move(from, to)

- **Preconditions**: {`At(robot, from)`}
- **Add Effects**: {`At(robot, to)`}
- **Delete Effects**: {`At(robot, from)`}

#### Action: PickUp(book, location)

- **Preconditions**: {`At(robot, location), At(book, location), HandEmpty`}
- **Add Effects**: {`Holding(book)`}
- **Delete Effects**: {`At(book, location), HandEmpty`}

#### Action: Place(book, location)

- **Preconditions**: {`At(robot, location), Holding(book)`}
- **Add Effects**: {`At(book, location), HandEmpty`}
- **Delete Effects**: {`Holding(book)`}

---

### Example Problem Instance

#### Initial State

- `At(robot, base)`
- `At(book, shelf)`
- `HandEmpty`

#### Goal State 

- `At(book, desk)`
