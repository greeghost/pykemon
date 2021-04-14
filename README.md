# Pykemon

## Presentation

Pykemon is a project made by me in order to offer automated tools linked with competitive pokemon battling.  
The project name comes from a blend of **Py**thon and Po**kemon**, with one of them being the main programming language used in this project, and the other one its main focus.

## A set of python scripts useful for pokemon-related projects.

### First use (setup)

The `db_gen.py` script lets you create a SQL database containing information scraped on [smogon](https://www.smogon.com/dex). An input is required in the form of a 2-character string with valid options being `ss`, `sm`, `xy`, `bw`, `dp`, `rs`, `gs` and `rb`. The expected syntax to launch the create the database is the following, with `ss` being the default option, as it is the most recent generation. The last available option is `all`, which builds all of the databases in the current directory.
```shell
$ python3 db_gen.py <option>
```

***Update :*** GS (Gold & Silver) and RB (Red & Blue) are not currently supported because since stats worked differently back then (no ability, no SpD nor SpA...), these two cause problems with the automation process.


All of the other scripts use the database to perform various actions.



## Changelog

- Latest Version 0.1.2  
April 13, 2021  
add tournament generation/upload/update support  
clean project architexture (database folder, assets folder)

- version : 0.1.1  
October 19, 2020  
Create the basics  
Created this `README`, defined some work to do.

- Version 0.0.2  
August 26, 2020  
calcs and scarves added

- Version 0.0.1  
March 28, 2020  
First draft, first sharing.  
db_gen code working




### TBA :

#### within README :

- Visuals
- Installation (when exported to the internet)
- Usage (when actually something to use)
- Support (contact?)
- Roadmap (future plans)
- Contributing (no real plan to at the moment, since I don't expect anyone to contribute with the state it is currently in, and the specific domain of interests this project covers)
- Authors and acknowledgment (thanking contributors)
- Project status

#### Outside :

- License
- Changelog
- Docs
