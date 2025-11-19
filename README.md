# Unit 3 of Aerospace Programming
## Libraries and File Formats

## Installing Requirements.
These files have various requirements, each of which are specified at the top of their respective file. These dependencies include astropy, matplotlib, spiceypy, astroquery, skyfield, and/or pandas.

I created these files to be run in a virtual environment to get around the pip3 "externally-managed-environment" error.
You can run set up the environment the same way I did by following these steps.

1. Set up the virtual environment. Within your project directory, open terminal and enter:

```python3 -m venv <your_project_name>  ```

2. Activate the environment, telling your computer to "look there" for the files.

```source <your_project_name>/bin/activate ```

3. Install the required library in the new virtual environment

```pip3 install <astropy/matplotlib/spiceypy/astroquery/skyfield/pandas>```

4. Check your install

```pip3 list```

5. When you're done, deactivate the virtual environment

```deactivate```

6. To restart the environment, repeat step 2 within your project directory.
