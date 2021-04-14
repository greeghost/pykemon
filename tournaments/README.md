# `.pkt`

## What is `.pkt`?

PKT is short for *PoKemon Tournament*. It is a custom-made file format used for
storing, loading and updating data about pokemon tournaments. Its goal is to
provide a way of describing them that makes these three tasks easy to do.

The ultimate goal of the `.pkt` project is to provide automatic scripts to
modify them without the need to get your hands in the `.pkt` files.

## Description of a `.pkt` file

Every `.pkt` file consists of 5 parts :

- A **Header** which describes the tournament stage (in `pool` stage, in `playoff` stage or `finished`)
- Two comma-separated integers which represent the **number of teams** and **number of pools** (in cases where the number of pools is equal to 1, it can be omitted)
- A list of **all team names**, one per line, with one `===\n` line left between each pool
- A list of the already decided **next matches**, one per line, with format `<team1> - <team2>`, where `<team>` represents a team name (already decided matches can only be in the stage the tournament is in, and will thus be incomplete if the tournament is in `pool` stage)
- A list of the **previous matches**, one per line, with format `<team1> - <team2> : <score1> - <score2>` where `<team>` represents a team name, and `<score>` an integer between 0 and 6 (at least one of them must be 0).

Here is an example of a valid `.pkt` document

~~~~~ (pkt)
pool

4, 2

A
B
===
C
D

A - B

C - D : 2 - 0
~~~~~
