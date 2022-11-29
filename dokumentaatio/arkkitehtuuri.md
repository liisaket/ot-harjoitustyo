```mermaid
 classDiagram
      Entry "*" --> "1" User
      class User{
          username
          password
      }
      class Entry{
          id
          date
          emotion
          content
      }
```

![Pakkausrakenne](./kuvat/arkkitehtuuri-rakenne.png)
