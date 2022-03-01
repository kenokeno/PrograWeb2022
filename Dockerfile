FROM jboss/wildfly
ADD MySite /opt/jboss/wildfly/welcome-content/
CMD ["/opt/jboss/wildfly/bin/standalone.sh", "-b", "0.0.0.0", "-bmanagement", "0.0.0.0"]