import click
import re
from models import database, User
from uuid import uuid4
from peewee import IntegrityError


def insert_admin(first_name, last_name, email, password):
    try:
        database.connect()

        new_admin = User.create(
            user_id=uuid4(), first_name=first_name, last_name=last_name,
            is_admin=True, email=email, password=password)

        database.close()
    except IntegrityError:
        return None

    return new_admin


def main():
    @click.command()
    @click.option('--firstname', prompt='Inser first name', help='First name of the new admin')
    @click.option('--lastname', prompt='Insert last name', help='Last name of the new admin')
    @click.option('--email', prompt='Insert email', help='Valid email address of the new admin (required)')
    @click.password_option('--password', prompt='Insert password', help='Password of the new admin (required)')
    def create_admin(firstname, lastname, email, password):
        """Create a new admin for the ecommerce"""
        # TODO: Check email with re module
        match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)
        if match == None:
            print('Email Not Valid')
        # TODO: Check email and password insert
    def crypt_password(password):
        crypt = pbkdf2_sha256.hash(password)

        return crypt

        new_admin = insert_admin(firstname, lastname, email, password)

        if new_admin is not None:
            pass
        else:
            pass

    create_admin()

if __name__ == '__main__':
    main()
