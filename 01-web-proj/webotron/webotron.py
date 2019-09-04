import boto3
import click

session = boto3.Session(profile_name='revaix')
s3 = session.resource('s3')

@click.group()
def cli():
    "Webotron deploys websites to AWS"
    pass

@cli.command('list-buckets')
def list_buckets():
    "List s3 buckets"
    for bucket in s3.buckets.all():
        print(bucket)

@cli.command('list-objects-s3')
@click.argument('bucket')
def list_objects(bucket):
    "List objects of a specific bucket"
    for object in s3.Bucket(bucket).objects.all():
        print(object)

if __name__=='__main__':
    cli()
