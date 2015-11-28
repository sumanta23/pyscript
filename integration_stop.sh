cd Certificate/testware
if -f .start
    ./target/jboss-as-7.1.1.Final/bin/jboss-cli.sh --connect ":shutdown"
fi
