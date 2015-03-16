# PyBak #

## Info ##

This is just a simple script I wrote to back a number of directories.
It is a little hacky and needs improvements, I plan to add ignored file support, 
and zipfile creation. Both of which are trivial but I'm lazy. This script will copy sub-directories so I hope that's what you want.

## Usage ##
This script has no command line interface you simply set the config data and run it. There is a yaml file in the config directory which you *must* edit. You can make a .bat file to run it and schedule it with the task scheduler.

#### data.yaml ####
```yaml

base_backup_dir : C:/Backups/{0}_{1}
jobs: [[Job1, 'C:/Important Files'], [Job2, 'C:/Files']]

```

- **base_backup_dir** Should be set to where you want your backups to be copied to. It is a format string so it must end in /{0}_{1} 
- **jobs** is a List of lists containing as many backup jobs as you need. Name them whatever you wish, something less ambiguous than *Job1* and *Job2*?

## Issues ##
This script has a couple of issues I should mention, it has a no tests, it has the structure of a python module but it isn't configured, so **PyYaml** but be downloaded before you use it and there is a relative path in the **parse_config** function that will need to be changed if you run the script with a batch file from the task scheduler.
I'm not sure about how to workaround this issue just yet.

```
pip install pyyaml
```


## Credits ##
This is an adaption of a script from a [Stack Exchange](http://codereview.stackexchange.com/questions/49351/python-back-up-script "Stack Exchange") Thread that I found. Thanks to the original author for saving me some time.

## License ##
This code is licensed under the MIT License.