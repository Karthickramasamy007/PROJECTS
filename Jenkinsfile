def img //Global variable
pipeline {

    environment {
        registry = "Karthickramasamy007/PROJECTS"
        registryCredentials = "docker_credentials"
        dockerImage = ""
    }

    agent any

    stages {

        stage("Chekout") {
            step{
                git 'https://github.com/Karthickramasamy007/PROJECTS.git'
            }

        }

        stage("Build Image") {
            step{
                script{
                    imt = registry + ":$env.BUILD_ID"
                    println ("${img}")
                    dockerImage = docker.build("${img}")
                }
            }
        }

        stage("testing") {
            step {
                sh 'docker run -d --name ${JOB_NAME} -p 5000:5000 ${img}'
            }
        }

        state("push to Docker hub") {
            step{
                script {
                    docker.withRegistry('https://registry.hub.docker.com',registryCredentials) {
                        dockerImage.push()
                    }
                }
            }
        }
    }
}
