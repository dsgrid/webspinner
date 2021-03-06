# webspinner
[![PyPI](https://img.shields.io/pypi/v/webspinner.svg)](https://pypi.python.org/pypi/webspinner/)

Python utilities for working with data source types used by the dsgrid project 
(i.e., AWS, PostgreSQL, and .parquet)

[Install](#install) | [Configure](#configure) | [Uninstall](#uninstall)

## Install

```bash
pip install webspinner
```

or 

```bash
pip install git+ssh://git@github.com/dsgrid/webspinner.git@v1.1.0
```

or 

```bash
pip install git+https://github.com/dsgrid/webspinner.git@master
```

To get dependencies required for certain types of resources, add extras as in:

```
pip install webspinner[pgres]
pip install webspinner[aws]
pip install webspinner[parquet]
pip install webspinner[pgres,aws,parquet]
```

## Configure

webspinner provides code in support of accessing various dsgrid data sources. 
That said, you may only need to access one or two data sources for your particular 
project. Please configure access to the resources you need.

[PostgreSQL](#posgresql) | [AWS](#aws) | [.parquet](#parquet)

### PosgreSQL

#### Dependencies

```
pip install pgpasslib psycopg2
```

Install [pgAdmin](https://www.pgadmin.org/download/) or another PostgreSQL client. 
Then identify or create your [pgpass file](https://www.postgresql.org/docs/9.1/static/libpq-pgpass.html). 
On Mac and Linux, the file to edit or create is `~/.pgpass`. On Windows it is 
`%APPDATA%/Roaming/postgresql/pgpass.conf`, where `%APPDATA%` is the AppData 
subdirectory under your user profile (i.e., `C:/Users/$USER/AppData`). If the 
file does not yet exist, simply create a new text file named `pgpass.conf`. 
Once the file exists, add the lines like:

```
POSTGRES_SERVER_ADDRESS:*:*:$USER:YOUR_PASSWORD
```

replacing `POSTGRES_SERVER_ADDRESS` with the PostgreSQL server to connect to, 
`$USER` with your actual username, and `YOUR_GISPGDB_PASSWORD` with your actual 
password. The dsgrid team typically connects to `10.20.5.28` or its alias 
`gds_edit.nrel.gov`.

**On Mac and Linux** be sure to set the permissions to

```
chmod 600 ~/.pgpass
```

If the permissions are too permissive, your run may not start.

#### Configuration file arguments

Project-specific defaults can be stored in a text file, e.g., `webspinner.config` 
or `config.ini` with a `[PGRES]` section and any or all of the following arguments:

```
[PGRES]
user = your_user_name
dbase = database_name
host = host_address
port = port_number
```

The defaults can then be loaded in at any time (e.g., at the top of a script or 
a notebook) by passing the configuration filepath into the `webspinner.configure` 
function.

### AWS

#### Dependencies

```
pip install pyathena awscli
```

Set up your AWS access credentials by issuing the following command in the terminal. 
(FYI there are [other ways](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/configuration.html#guide-configuration) 
to set up your credentials if you're interested.)

```
>> aws configure
AWS Access Key ID [None]: <your key>
AWS Secret Access Key [None]: <your secret key>
Default region name [None]: us-west-2
Default output format [None]: json
```

#### Configuration file arguments

Project-specific defaults can be stored in a text file, e.g., `webspinner.config` 
or `config.ini` with an `[AWS]` section and any or all of the following arguments:

```
[AWS]
s3_staging_dir = data_staging_dir_on_s3
region_name = aws_region_name
schema_name = aws_database_schema_name
work_group = aws_work_group_name
```

The defaults can then be loaded in at any time (e.g., at the top of a script or 
a notebook) by passing the configuration filepath into the `webspinner.configure` 
function.

### .parquet

If you plan to work with .parquet files, also install pyarrow.

```
pip install pyarrow
```

## Uninstall

```
pip uninstall webspinner
```

