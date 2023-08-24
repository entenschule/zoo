# property maker

Example command to be run in _zoo_ folder:<br>
`python proj/machinery/prop_maker animals.cat whiskers`

This will create the folder [animals/cat/properties/whiskers](../../animals/cat/properties/whiskers)
and the files in it, especially the [init file](../../animals/cat/properties/whiskers/__init__.py).<br>
It will also create a [SUCCESS.md](SUCCESS.md) in this folder, which contains a link to the created folder.

The first argument is the path to the class folder,
and the second one is the name of the property to be added.<br>
(It is assumed, that the class is nested in [_proj_](../../../proj), and that it has a _properties_ folder.)
