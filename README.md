# Secret Santa

#### Purpose: create a series of matches from a list of people and automatically notify participants of their match

##### Usage:
1. Create a list of participants, each on their own line.
  * Format: (name)|(e-mail address)
2. Save the file as "participants.txt" in the same directory as the program.
3. Run the program with your e-mail server, address, and password (more help with the "--help" flag).

The program will ensure that nobody will be matched with themselves and that if Person A gets Person B, Person B will not get Person A.

Each match is sent out to the appropriate participant. A list of matches is also generated as "matches.txt" in the same directory. Warning: reading through it will spoil the surprise!
