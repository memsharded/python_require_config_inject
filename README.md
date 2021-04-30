# python_require_config_inject

Possibilities to inject a new package configuration, e.g. for a new hardware, and get the same recipe revision, but new binaries.
The new package configurations are not known when the package was first created, they are added after the recipe and some binary packages have been created.


## option_approach

- Using a ``options = {"hardware": "ANY"}`` that receives a versioned file

```
cd option_approach
python build.py
```

The option values must be absolute paths, that recipes can load from disk to ``build()`` the binaries correctly.
The only limitation, is that it doesn't allow arbitrary changes to the hw configuration files without versioning them.

Output is clear:
```
Package_ID: d4532e22829c43b15eaf736956032cecb5f4f136
        [options]
            hardware: hw1_v1.0
        [settings]
            arch: x86_64
            build_type: Release
            compiler: Visual Studio
            compiler.runtime: MD
            compiler.version: 16
            os: Windows
        Outdated from recipe: False

    Package_ID: d4d291d15ceb5ef4d25bcd70769584e30547121a
        [options]
            hardware: hw1_v1.1
        [settings]
            arch: x86_64
            build_type: Release
            compiler: Visual Studio
            compiler.runtime: MD
            compiler.version: 16
            os: Windows
        Outdated from recipe: False

    Package_ID: e5cfd75e0adb1b54a1810f7a746d34a22a652e1b
        [options]
            hardware: hw2_v1.0
        [settings]
            arch: x86_64
            build_type: Release
            compiler: Visual Studio
            compiler.runtime: MD
            compiler.version: 16
            os: Windows
        Outdated from recipe: False
```

## settings_approach

Not implemented here, but seems totally doable, very similar to the option_approach, but being defined at the ``settings.yml``, with the possibility to define it globally to all or many packages in the recipe


## python_require approach

FAILED attempt.
The ``python_requires`` mechanism is common to the recipe. Anything that is injected there would be affecting the recipe and all binaries of the recipe.


## conandata.yml approach

If we put configuration specific data in ``conandata.yml``, that will cause a new recipe revision, making "old" revisions previously existing binaries.
This approach would be valid only if:

- We can add all the configurations we want at once in the ``conandata.yml``
- We want to rebuild all the configurations from sources again, for the newly generated recipe revision
