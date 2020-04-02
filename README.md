standardnotes-tools
===================

[Standard Notes](https://standardnotes.org/) is a free, open source and multiplatform notes app.
As an another advantage, it comes with a well-designed JSON format used for ex/import of all user data in Standard Notes.

This repo contains some tools for Standard Notes.


Things to keep in mind
----------------------

* Unfortunately, after importing a JSON file twice, the notes will be present twice.
  Though the files uniquely identify every note through a UUID, that is not used and new UUIDs are given.
  Thus it's not possible to simply externally modify and then re-import the notes.
  However, Standard Notes provides a way to completely reset the account (without loosing Extended status), and as the JSON contains all user data, that works actually pretty good.


License
-------

See [LICENSE.md](LICENSE.md).

