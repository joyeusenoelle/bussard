import feedparser
import opyml
import psycopg2

def read_archive(self, filename):
    with open(filename, "r") as file:
        contents = file.read(filename)