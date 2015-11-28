cd Certificate/testware
if [ -f .start]
then
    echo "stopping server"
    ./target/jboss-as-7.1.1.Final/bin/jboss-cli.sh --connect ":shutdown"
fi
