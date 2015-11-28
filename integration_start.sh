git clone https://github.com/sumanta23/Certificate.git Certificate

cd Certificate

sudo pip install virtualenv; virtualenv .venv; source .venv/bin/activate; pip install -r testware/requirements.txt

python testware/certgen.py testware

mvn clean install -P jboss_managed_local

cd testware

cp target/arquillian/_DEFAULT__certificate-ear_Certificate-ear-2.0.ear target/jboss-as-7.1.1.Final/standalone/deployments/

touch .start
./target/jboss-as-7.1.1.Final/bin/standalone.sh -c standalone-full-sam.xml &
