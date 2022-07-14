# OSLShadersForRenderMan
Siggraph 2022 Course Supplementary Material

# Requirements
* [Pixar's RenderMan](https://renderman.pixar.com)

# Instructions
1. Set up RenderMan:

    1. Install [RenderManProServer](https://renderman.pixar.com/store) and ensure it is functioning properly.

    1. Optionally install a [RenderMan Bridge Application](https://renderman.pixar.com/bridge-tools) and its associated RenderMan plugin and ensure they are functioning properly.

1. Set these environment variables appropriately. These are required by the [make](https://www.gnu.org/software/make/manual/) system that's used to compile and install the shaders:
    * PIXAR_ROOT
    * RMAN_VERSION

    For example, if your version of RenderManProServer is installed in
    `/opt/pixar/RenderManProServer-24.4`, then:

    ```shell
    PIXAR_ROOT = /opt/pixar
    RMAN_VERSION = 24.4
    ```
1. Download or [clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) this repository.
1. `cd` into the dowloaded or cloned repository's directory.

At this point, you can use the `make` or `make all` command (they are equivalent) to build the shaders.
You can also `cd osl` into the osl directory and `make` the shaders there.
The osl/Makefile will only make .oso files for .osl files that are more recent than their complied .oso file.
In this way, you can edit a .osl file and execute `make` from the osl directory and only the updated .osl file(s) will be built.

`make clean` and `make help` can also be executed from either the top-level directory or the osl directory.
`make clean` removes the built shaders, and `make help` provides additional information about the make system and how it's controlled.

Once built, the shaders can be used in [RenderMan](https://rmanwiki.pixar.com/display/REN24/RenderMan) or a [RenderMan Bridge Application](https://renderman.pixar.com/bridge-tools) by setting the RMAN_SHADERPATH environment variable to include the location of the built shaders.

For example, if you downloaded or cloned this repository to `$HOME/OSLShadersForRenderMan`, then set
```shell
RMAN_SHADERPATH = "$(HOME)/OSLShadersForRenderMan/build/$(RMAN_VERSION)/shaders:$(RMAN_SHADERPATH)"
```
so that RenderMan will find these shaders, along with the Pixar shaders.

Note that [RenderMan for Maya](https://rmanwiki.pixar.com/display/RFM24) requires additional setup to use [Custom Shading Nodes](https://rmanwiki.pixar.com/display/RFM24/Installing+Custom+Nodes).

# License
Licensed under either of

* Apache License, Version 2.0, ([LICENSE-APACHE](LICENSE-APACHE) or http://www.apache.org/licenses/LICENSE-2.0)
* MIT license ([LICENSE-MIT](LICENSE-MIT) or http://opensource.org/licenses/MIT)

at your option.
