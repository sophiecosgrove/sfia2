pipeline{
    agent any
    stages{
        stage("Make scripts executable"){
            steps{
                sh 'chmod +x ./script/*'
            }
        }
        stage("Source variables"){
            steps{
                sh '
            }
        }
        stage("Deploy Docker Swarm Stack"){
            steps{
                sh './script/docker.sh'
            }
        }
    }
}