"""
Exercise 3 - Songs and Playlists (Composition)  (SOLUTION)
----------------------------------------------
A Playlist HAS many Song objects.

Song(title, artist, seconds)
  str(song)        -> "Title by Artist (3:05)"   <- seconds shown as m:ss
  song.minutes()   -> seconds / 60 as a float

Playlist(name)
  add(song)                 add a Song to the end
  remove(title)             remove the first song with that title; return True if removed, else False
  total_seconds()           sum of all song lengths
  duration()                total as "m:ss", e.g. "7:42"
  longest()                 the longest Song (None if empty)
  by_artist(artist)         list of Songs by that artist (in playlist order)
  artists()                 SORTED list of unique artists
  len(playlist)             number of songs
  str(playlist)             "Road Trip (3 songs, 11:09)"

Hint: write a helper function format_time(seconds) -> "m:ss" and use it in
both classes. f"{s:02}" pads a number to 2 digits (5 -> "05").
"""


def format_time(seconds):
    # TODO
    pass


class Song:
    def __init__(self, title, artist, seconds):  # given
        self.title = title
        self.artist = artist
        self.seconds = seconds

    def minutes(self):
        # TODO
        pass

    def __str__(self):
        # TODO
        pass


class Playlist:
    def __init__(self, name):  # given
        self.name = name
        self.songs = []

    def add(self, song):
        # TODO
        pass

    def remove(self, title):
        # TODO
        pass

    def total_seconds(self):
        # TODO
        pass

    def duration(self):
        # TODO
        pass

    def longest(self):
        # TODO
        pass

    def by_artist(self, artist):
        # TODO
        pass

    def artists(self):
        # TODO
        pass

    def __len__(self):
        # TODO
        pass

    def __str__(self):
        # TODO
        pass


# ----------------------- Checks (don't change below) -----------------------
def check(label, get_actual, expected):
    try:
        actual = get_actual()
    except Exception as e:
        print(f"FAIL  {label}: crashed with {type(e).__name__}: {e}")
        return
    if actual == expected:
        print(f"PASS  {label}")
    else:
        print(f"FAIL  {label}: expected {expected!r}, got {actual!r}")


def make_playlist():
    p = Playlist("Road Trip")
    p.add(Song("Here Comes the Sun", "The Beatles", 185))
    p.add(Song("Bohemian Rhapsody", "Queen", 355))
    p.add(Song("Let It Be", "The Beatles", 243))
    return p


def after_remove():
    p = make_playlist()
    p.remove("Let It Be")
    return p.total_seconds()


song = Song("Here Comes the Sun", "The Beatles", 185)
check("format_time(185)", lambda: format_time(185), "3:05")
check("str(song)", lambda: str(song), "Here Comes the Sun by The Beatles (3:05)")
check("minutes()", lambda: round(song.minutes(), 2), 3.08)
check("len(playlist)", lambda: len(make_playlist()), 3)
check("total_seconds", lambda: make_playlist().total_seconds(), 783)
check("duration", lambda: make_playlist().duration(), "13:03")
check("longest", lambda: make_playlist().longest().title, "Bohemian Rhapsody")
check("by_artist", lambda: [s.title for s in make_playlist().by_artist("The Beatles")], ["Here Comes the Sun", "Let It Be"])
check("artists", lambda: make_playlist().artists(), ["Queen", "The Beatles"])
check("str(playlist)", lambda: str(make_playlist()), "Road Trip (3 songs, 13:03)")
check("remove existing", lambda: make_playlist().remove("Let It Be"), True)
check("remove missing", lambda: make_playlist().remove("Yesterday"), False)
check("total after remove", after_remove, 540)
check("longest of empty", lambda: Playlist("Empty").longest(), None)
