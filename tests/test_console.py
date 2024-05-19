#!/usr/bin/python3
"""Module for TestHBNBCommand class."""

from console import HBNBCommand
from models.engine.file_storage import FileStorage
import unittest
import datetime
from unittest.mock import patch
import sys
from io import StringIO
import re
import os


class TestHBNBCommand(unittest.TestCase):
    """
        Tests HBNBCommand console

    """

    def setUp(self):
        print("Testing Console methods")

    def test_help_quit(self):
        """Tests the help command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
        ser = 'Quit command to exit the program\n'
        self.assertEqual(ser, f.getvalue())

    def test_help_create(self):
        """Tests the create command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
        ser = 'Creates a new instance\n'
        self.assertEqual(ser, f.getvalue())

    def test_help_clear(self):
        """Tests default"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help clear")
            ser = 'Clear the screen\n'
            self.assertEqual(ser, f.getvalue())

    def test_help_show(self):
        """Tests show"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
            ser = 'prints the string representation of an instance\n'
            self.assertEqual(ser, f.getvalue())

    def test_help_destroy(self):
        """Tests destroy"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help destroy")
            ser = 'Deletes an instance based on the class name and id\n'
            self.assertEqual(ser, f.getvalue())

    def test_help_all(self):
        """Tests All"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help all")
            ser = 'Prints all string representation of all instances\n'
            self.assertEqual(ser, f.getvalue())

    def test_help_update(self):
        """Tests Update"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help update")
            ser = ' Updates the class\n'
            self.assertEqual(ser, f.getvalue())

    def test_help_count(self):
        """Tests count"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help count")
            ser = 'counts\n'
            self.assertEqual(ser, f.getvalue())

    def test_help_EOF(self):
        """End of line"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help EOF")
            ser = 'Handles EOF\n'
            self.assertEqual(ser, f.getvalue())

    def test_help_emptyline(self):
        """Tests empty line"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help emptyline")
            ser = '*** No help on emptyline\n'
            self.assertEqual(ser, f.getvalue())

    def test_help_default(self):
        """default"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help default")
            ser = '*** No help on default\n'
            self.assertEqual(ser, f.getvalue())


if __name__ == "__main__":
    unittest.main()
