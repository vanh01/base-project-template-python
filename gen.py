import click
import os

@click.group()
def cli():
    pass

@click.command()
def gen_service():
    """Generate a new service file to deploy server on linux"""
    basedir = os.path.abspath(os.path.dirname(__file__))
    if os.path.exists("flaskapp.service"):
        os.remove("flaskapp.service")
    str = f"""[Unit]
Description=A template for flask web service
After=network.target

[Service]
WorkingDirectory={basedir}
Environment= "PATH={basedir}/venv/bin"
ExecStart={basedir}/venv/bin/gunicorn --workers 3 --bind unix:app.sock -m 007 app:app

[Install]
WantedBy=multi-user.target"""
    f = open("flaskapp.service", "w")
    f.write(str)
    f.close()

cli.add_command(gen_service)

if __name__ == "__main__":
    cli()