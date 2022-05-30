pipeline {
    agent any

    triggers {
        pollSCM('*/5 * * * 1-5')
    }
    options {
        skipDefaultCheckout(true)
        // Keep the 10 most recent builds.
        buildDiscarder(logRotator(numToKeepStr: '10'))
        timestamps()
    }
    environment {
      PATH="/var/lib/jenkins/miniconda3/bin:$PATH"
      registry = "Karthickramasamy007/PROJECTS"
      registryCredentials = "docker_credentials"
      dockerImage = ""
        
    }

    stages {

        stage("Chekout") {
            steps{

                git branch: 'main', credentialsId: 'f11f8219-de25-4d29-8e44-39273b24b1d0', url: 'https://github.com/Karthickramasamy007/PROJECTS.git'

            }

        }

        stage("Build Image") {
            steps{
                script{
                    img = registry + ":$env.BUILD_ID"
                    println ("${img}")
                    dockerImage = docker.build("${img}")
                }
            }
        }

        stage("testing") {
            steps {
                sh 'Docker run -d --name ${JOB_NAME} -p 5000:5000 ${img}'
            }
        }

        stage("push to Docker hub") {
            steps{
                script {
                    docker.withRegistry('https://registry.hub.docker.com',registryCredentials) {
                        dockerImage.push()
                    }
                }
            }
        }
    }


        
        post {
            always {
                echo 'always print'
            }
            failure {
                echo "Send e-mail, when failed"
            }
        }

}
