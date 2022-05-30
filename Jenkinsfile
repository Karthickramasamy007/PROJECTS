pipeline {
    agent any
    stages {
        stage('Build') {
            agent {
                docker {
                    RUN curl -fsSLO https://get.docker.com/builds/Linux/x86_64/docker-17.04.0-ce.tgz \
                      && tar xzvf docker-17.04.0-ce.tgz \
                      && mv docker/docker /usr/local/bin \
                      && rm -r docker docker-17.04.0-ce.tgz
                    image 'gradle:6.7-jdk11'
                    // Run the container on the node specified at the
                    // top-level of the Pipeline, in the same workspace,
                    // rather than on a new node entirely:
                    reuseNode true
                }
            }
            steps {
                sh 'gradle --version'
            }
        }
    }
}
