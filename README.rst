Building Docker from Docker
===========================

When running a double-dutch_-style build,
a naive implementation will often end
up playing all kinds of mount games
which expose platform details.
For example, with Docker Mac,
it depends on the folders mounted
into the container VM.

An alternative is to run the build
from inside the containers,
and use "ADD".


Demo
----
.. code::

    docker build -t gruilder -f build.docker . && \
    docker run -v /var/run/docker.sock:/var/run/docker.sock --rm -it gruilder && \
    docker run --rm -it -p 80:80 greeter

.. _double-dutch: https://glyph.twistedmatrix.com/2015/03/docker-deploy-double-dutch.html
