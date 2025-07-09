# bussard

is an RSS aggregator and (eventually) reader. Right now it just aggregates, and it doesn't do that well.

The intent is to build a FastAPI-based system that will regularly pull in the content from RSS feeds, update the database with the new items, and then display either only unseen items or all items, depending on what the user selects. I'm using FastAPI because it's what we're moving to at work, and I like getting practice outside the work environment.

## The name

is from nuclear physicist [Robert Bussard](https://en.wikipedia.org/wiki/Robert_W._Bussard). Bussard came up with a theoretical fusion drive, a Bussard ramjet, that could travel through interstellar space by collecting ionized hydrogen from the interstellar gas, fusing it in a reactor, and then using the reactor's exhaust to propel the ship. *Star Trek* later adopted part of this; the spinning domes (later red lights) at the front of the starships' warp nacelles are *Bussard ramscoops*, which collect the interstellar hydrogen and feed it to the engines.

Since this project performs a similar function, only with information instead of atoms and reading RSS feeds instead of traveling through space, I thought it was appropriate.

## Contributing

is pretty easy; please see [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## Licensing

is likewise simple. <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>. This means:

* You may use this code, or any portion of it, in your own works.
* If you do so, you MUST:
    * Give credit to the original author.
    * Make the source code of the work that incorporates this code freely available.
* If you do so, you MAY:
    * Make your project commercially available (i.e. charge money for it).
