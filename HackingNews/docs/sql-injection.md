Das angreifbare input field ist die Suchleiste auf */authors*

### Das hinterlegte Select sieht wie folgt aus:

`SELECT username, email FROM user WHERE username LIKE '%{search}%'`

Dabei ist `{search}` die Einfügung aus der Suchleiste. An dieser Stelle wird also injected.

### Es können beispielsweise folgende Injections gemacht werden:

-   Alle Benutzernamen und zugehörigen Passwörter werden ausgegeben:  
    `%' UNION SELECT username, password FROM user -- `

---

Es kann auch der Zugang als anderer Benutzer mit SQL-Injection erschlichen werden. Das angreifbare Input-Field ist das Eingabefeld des Benutzernamens auf `/login`

### Das hinterlegte Select sieht wie folgt aus:

`SELECT id FROM user WHERE username='{username}' and email='{email}' and password='{password}';`

Dabei ist `{username}` die Einfügung aus dem Eingabefeld des Benutzernamens. An dieser Stelle wird also injected.

**Wichtig:** die anderen Input-Felder müssen trotzdem gültige Werte bekommen! Die Werte können aber beliebig sein, solange sie die allgemeinen Kriterien erfüllen:
- Email theoretisch gültig und nicht leer
- Passwort mindestens 4 Zeichen

### Es können beispielsweise folgende Injections gemacht werden:

-   Anmelden als beliebiger Benutzer
    `a' OR 1=1 LIMIT 1 -- `

-   Anmelden als Benutzer mit bestimmter id
    `a' OR 1=1 AND id=1 -- `

---