from invoke import task


@task
def start(ctx):
    ctx.run("flask --app src/app.py run", pty=True)

@task
def lint(ctx):
    ctx.run("pylint src", pty=True)

@task
def test(ctx):
    ctx.run("pytest src", pty=True)
