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
            steps{
                git 'https://github.com/Karthickramasamy007/PROJECTS.git'
            }

        }

        stage("Build Image") {
            steps{
                script{
                    imt = registry + ":$env.BUILD_ID"
                    println ("${img}")
                    dockerImage = docker.build("${img}")
                }
            }
        }

        stage("testing") {
            steps {
                sh 'docker run -d --name ${JOB_NAME} -p 5000:5000 ${img}'
            }
        }

        state("push to Docker hub") {
            steps{
                script {
                    docker.withRegistry('https://registry.hub.docker.com',registryCredentials) {
                        dockerImage.push()
                    }
                }
            }
        }
    }
}
