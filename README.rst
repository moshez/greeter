Building Docker from Docker
===========================

Demo
----
.. code::

    docker build -t gruilder -f build.docker . && \
    docker run -v /var/run/docker.sock:/var/run/docker.sock --rm -it gruilder && \
    docker run --rm -it -p 80:80 greeter
