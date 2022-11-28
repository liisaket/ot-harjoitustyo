Tietokannat:

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
Arkkitehtuuri:

![Pakkausrakenne](./kuvat/arkkitehtuuri-rakenne.png)
