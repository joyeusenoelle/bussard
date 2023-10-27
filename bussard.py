import feedparser
import opyml
import psycopg2


def read_archive(self, filename):
    # filename is assumed to be relative to the directory you're calling this
    # from, or globally qualified. It cannot be a URL or non-local file.
    with open(filename, "r") as file:
        contents = file.read(filename)
