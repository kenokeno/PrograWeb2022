FROM jboss/wildfly
ADD MySite /opt/jboss/wildfly/welcome-content/
CMD ["/opt/jboss/wildfly/bin/standalone.sh", "-b", "0.0.0.0", "-bmanagement", "0.0.0.0"]

USER root

# Add the WildFly distribution to /opt, and make wildfly the owner of the extracted tar content
# Make sure the distribution is available from a well-known place
RUN yum install epel-release \
    && yum install python-pip \
    && pip install selenium==3.141.0