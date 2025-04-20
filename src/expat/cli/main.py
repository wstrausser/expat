from expat.init_schema import schema_up

import click

import sqlite3


@click.group("expat")
def main():
    pass

@main.command("test")
def test():
    flavour = "sqlite"
    connection = sqlite3.connect("scratch/test.db")
    schema_up(connection, flavour)
