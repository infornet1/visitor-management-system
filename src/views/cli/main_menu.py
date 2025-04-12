import click
from datetime import datetime
from src.controllers.visitor_controller import VisitorController
from src.models.visitor import Visitor

@click.group()
def cli():
    """Visitor Management System CLI"""
    pass

@cli.command()
@click.option('--first-name', prompt='First Name', help='Visitor first name')
@click.option('--last-name', prompt='Last Name', help='Visitor last name')
@click.option('--email', prompt='Email', help='Visitor email')
@click.option('--phone', prompt='Phone', help='Visitor phone number')
@click.option('--purpose', prompt='Purpose of visit', help='Reason for visiting')
def check_in(first_name, last_name, email, phone, purpose):
    """Check in a new visitor"""
    visitor_data = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'phone': phone,
        'purpose': purpose,
        'check_in': datetime.now()
    }
    visitor = VisitorController.create_visitor(visitor_data)
    click.echo(f"Visitor {visitor.first_name} {visitor.last_name} checked in successfully!")

if __name__ == '__main__':
    cli()