\page conductor Conductor

The PROS CLI conductor is used to manage PROS projects. View available commands by running `pros conductor` (alias `pros c`).

NOTE: Adding custom depos is currently not official supported and will be overhauled in a coming update.

### Creating a project

To create a new project, navigate to the desired directory and run:

```
$ pros conductor new-project [project-name]
```

Where `[project-name]` is the name of the project, a PROS project with the name will be created.

You can specify additional options, such as kernel version with the following format:

```
$ pros conductor new-project [project-name] [target] [kernel version]
```

### Installing a template

First, download the tempalte zip file. Move the zip file to you PROS project folder. 
Then run these commands to apply the template.
```
$ pros conductor fetch [template name]@[version]
$ pros conductor apply [template name]@[version]
```

